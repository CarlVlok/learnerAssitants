import gemConnect as gc
from chat import fileChat

input = "What is the main theme of all given context"
module = "FIT152"
user="Carl"
chat=1
output = gc.agent(input, module)

print(output)

c = chat.filechat(user, input)

c.newChat()


