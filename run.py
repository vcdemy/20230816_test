from fastapi import FastAPI
import gradio as gr

app = FastAPI()

def hello(name):
    return f"Hello {name}!"

demo = gr.Interface(hello, 'text', 'text')
app = gr.mount_gradio_app(app, demo, path="/")