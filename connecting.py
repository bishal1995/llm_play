import os
from pyexpat import model
from openai import OpenAI, api_key, responses
from dotenv import load_dotenv
from pprint import pprint

# load_dotenv()
# api_key=os.getenv('OPENAI_API_KEY')

# if not api_key:
#     raise ValueError('No API key found')
# else:
#     print('Found the API Key')

local_model = "qwen3:latest"
client=OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="not-needed"
)

def ask_chatgpt(user_message):
    response = client.chat.completions.create(
        model=local_model,
        messages=[
            {
                "role": "system",
                "content": "You are sarcastic agent"
            },
            {
                "role": "user",
                "content" : user_message,
            },
        ],
        temperature=0
    )
    pprint(response.choices[0].message)

user_message = "Who is the most powerful person in India"
response = ask_chatgpt(user_message=user_message)
