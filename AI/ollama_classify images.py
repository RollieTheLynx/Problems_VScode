# -*- coding: utf-8 -*-
"""
https://github.com/ollama/ollama-python
ollama run gemma4:26b
ollama run qwen2.5-coder:14b

"""
import ollama
import os

def classify_image_locally(image_path):
    try:
        res = ollama.chat(
            model='gemma4:e4b',
            # model='gemma4:26b',
            messages=[{
                'role': 'user',
                'content': 'Is this image a drawing or real photo? Answer drawing or photo',
                'images': [image_path]
            }]
        )
        return res['message']['content']
    except Exception as e:
        return f"Error: {e}"

def classify_images_in_folder(folder_path):
    # Iterate over each file in the specified folder
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image_path = os.path.join(folder_path, filename)
            print(classify_image_locally(image_path))


# Usage
# print(classify_image_locally("E:\\lulz\\Maki\\1357989098053.png")) #dr
# print(classify_image_locally("E:\\lulz\\4cObpTM1TAg.jpg")) #dr
# print(classify_image_locally("E:\\lulz\\8xCtDNYq5Vc.jpg")) #dr
# print(classify_image_locally("E:\\lulz\\1371934593428.jpg")) #ph
# print(classify_image_locally("E:\\lulz\\1372458837366.jpg")) #ph
# print(classify_image_locally("E:\\lulz\\1373488852963.png")) #ph
# print(classify_image_locally("E:\\lulz\\Horo cup.jpg")) #ph

folder_path = 'E:\\lulz\\China'
classify_images_in_folder(folder_path)