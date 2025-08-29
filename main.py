import gemConnect as gc
import chat
import dataLoad as dl


input = "What is the main theme of all given context"
module = "FIT152"
user="Carl"
bot = gc.agent()
response = bot.query(input, module)
