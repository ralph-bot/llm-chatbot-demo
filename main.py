import os 
import sys
from ollama_unit import *
#from speech_unit import *
import gradio as gr
import numpy as np
import librosa
import whisper


def tts(text):
    pass


def speech2text(mic=None, file=None):
    if mic is not None:
        audio = mic
    elif file is not None:
        audio = file
    else:
        return "You must either upload a file or record audio."
      
    model = whisper.load_model("base")
    result = model.transcribe(audio)
    return result["text"]

def qa(mic=None, file=None):
    text = speech2text(mic,file)
    print("the asr text is ",text)
    #return text
    # call the ollama
    response = ollama_chat('llama3.2',text)
    print("response is ",response)
    return response



app = gr.Interface(
    qa,
    gr.Audio(sources="microphone",type='filepath'),
    "text",
    )

# app = gr.Interface(
#     fn=qa,
#     inputs=[gr.components.Audio(label="Speech"), gr.components.Textbox(lines=2, placeholder="What's your name?")],
#     outputs="text"
# )



if __name__ == "__main__":
    app.launch()
    #app.launch(server_name="0.0.0.0", server_port=2222)
