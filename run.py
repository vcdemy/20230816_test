from fastapi import FastAPI
import gradio as gr

app = FastAPI()

@app.get("/")
async def root():
    return "Gradio app is running at /gradio", 200

def hello(name):
    return name

demo = gr.Interface(hello, 'text', 'text')

app = gr.mount_gradio_app(app, demo, path="/gradio")