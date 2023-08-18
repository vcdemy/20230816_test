import gradio as gr

def hello(name):
    return f"Hello {name}!"

gr.Interface(hello, 'text', 'text').launch(server_port=5000, server_name="0.0.0.0")