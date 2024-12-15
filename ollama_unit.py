
import ollama
import json
# import bs4




def ollama_chat(model_name='llama3.2',ques = "" ):
    message_ques = [{'role': 'user', 'content': ques},]
    response = ollama.chat(model_name,message_ques)
    return response['message']['content']
#print(ollama.list())




# ques = '为什么天空是蓝色的？'
# response = ollama_chat('llama3.2',ques)
# print(response)


# from ollama import Client
# client = Client(host='http://localhost:11434')
# response = client.chat(model='llama3.1', messages=[
#   {
#     'role': 'user',
#     'content': '为什么天空是蓝色的？',
#   },
# ])