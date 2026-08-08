# -*- coding: utf-8 -*-
"""
https://github.com/ollama/ollama-python
ollama run gemma4:26b-a4b-it-q8_0
ollama run qwen2.5-coder:14b

"""
from ollama import chat

response = chat(
    model='gemma4:26b-a4b-it-q8_0',
    messages=[{'role': 'user', 'content': 'Explain how to cook pancakes'}],
)
print(response.message.content)
