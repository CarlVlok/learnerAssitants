from flask import Flask, render_template, request, session, redirect, url_for
import gemConnect as gc
import dataLoad
from chat import Chat
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

dl = dataLoad.dataLoad()
bot = gc.agent()

def load_chat_history(session):
    chat_dir = f"data/chats/{session}Chats"
    history = []
    if not os.path.exists(chat_dir):
        return history
    codes = os.listdir(chat_dir)
    for code in codes:
        with open(f"{chat_dir}/{code}", 'r') as file:
            lines = file.readlines()
            q, a = None, None
            for line in lines:
                if line.lower().startswith('question:'):
                    q = line.split(":", 1)[1].strip()
                elif line.lower().startswith('answer:'):
                    a = line.split(":", 1)[1].strip()
            if q and a:
                history.append({'question': q, 'answer': a})
    return history

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('user')
        module = request.form.get('module')
        session['user'] = user
        session['module'] = module

        chat_dir = f"data/chats/{user}Chats"
        if not os.path.exists(chat_dir):
            c = Chat(user, True)  # Create new chat directory
            session['chat_history'] = []
        else:
            c = Chat(user, False)
            session['chat_history'] = load_chat_history(user)
        return redirect(url_for('chat'))
    return render_template('landing.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if 'user' not in session or 'module' not in session:
        return redirect(url_for('login'))

    user = session['user']
    module = session['module']
    c = Chat(user, False)

    if request.method == 'POST':
        prompt = request.form.get('prompt')
        if prompt:
            ans = []
            response = bot.query(prompt, module, ans)
            answer = response[0]['answer'] if response else "No answer"
            # Write to chat file
            code = c.writeToNewChat(prompt, answer)
            # Update session chat history
            session['chat_history'].append({'question': prompt, 'answer': answer})
            session.modified = True
            return redirect(url_for('chat'))

    return render_template('index.html', chat_history=session.get('chat_history', []), user=user, module=module)

if __name__ == '__main__':
    app.run(debug=True)