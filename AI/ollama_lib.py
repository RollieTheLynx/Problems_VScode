# -*- coding: utf-8 -*-
"""
https://github.com/ollama/ollama-python


"""

from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='deepseek-r1:14b', messages=[
  {
    'role': 'user',
    'content': 'Explain in one paragraph why hunters are the worst class in WoTLK',
  },
])
# print(response['message']['content'])
# # or access fields directly from the response object
print(response.message.content)