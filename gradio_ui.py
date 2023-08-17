import gradio as gr

def hello(name):
    return name

demo = gr.Interface(hello, 'text', 'text')