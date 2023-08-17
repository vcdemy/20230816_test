import gradio as gr

def hello(name):
    return f"Hello {name}!"

gr.Interface(hello, 'text', 'text').launch()