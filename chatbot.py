import openai
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = API_KEY



# log = []

# while True:
#     usermessage = input()
#     if usermessage == 'end':
#         break
#     else:
#         log.append({'role':'user', 'content':usermessage}) ------> This for continously messages
#         respone = openai.ChatCompletion.create(
#             model = 'gpt-3.5-turbo',
#             messages = usermessage
#         )
# response = respone['choices'][0]['message']['content']
# print(respone)

def get_message(usermessage):
    usermessage = usermessage

    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = usermessage.text
    )
    response = response['choices'][0]['message']['content']
    return response