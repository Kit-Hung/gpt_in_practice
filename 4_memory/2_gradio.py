# 利用 Gradio 快速构建原型
import os
import gradio as gr
from openai import OpenAI

model = "gpt-3.5-turbo"
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ["OPENAI_BASE_URL"],
)


def get_response(inputs):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an AI assistant."},
            {"role": "user", "content": inputs},
        ],
        temperature=0.9,
        max_tokens=200,
    )
    return response.choices[0].message.content


def respond(message, chat_history):
    bot_message = get_response(message)
    # 保存历史对话记录，用于显示
    chat_history.append((message, bot_message))
    return "", chat_history


with gr.Blocks() as block:
    # 对话框
    chatbot = gr.Chatbot(height=240)
    # 输入框
    msg = gr.Textbox(label="Prompt")
    # 提交按钮
    btn = gr.Button("Submit")
    # 提交
    btn.click(respond, inputs=[msg, chatbot], outputs=[msg, chatbot])
    msg.submit(respond, inputs=[msg, chatbot], outputs=[msg, chatbot])

gr.close_all()
block.launch()
