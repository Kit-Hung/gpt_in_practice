import os
import gradio as gr
from openai import OpenAI

model = "gpt-3.5-turbo"
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ["OPENAI_BASE_URL"],
)

def get_response(msg):
    response = client.chat.completions.create(
        model=model,
        messages=msg,
        temperature=0.9,
        max_tokens=600,
    )
    return response.choices[0].message.content


def history_to_prompt(chat_history):
    # 讲对话内容保存在一个 list 里
    msg = [{
        "role": "system",
        "content": "You are an AI assistant."
    }]

    i = 0
    # 将 list 里的内容，组成 ChatCompletion 的 messages 部分
    # {role, content} dict
    for round_trip in chat_history:
        msg.append({"role": "user", "content": round_trip[0]})
        msg.append({"role": "assistant", "content": round_trip[1]})
    return msg

def respond(message, chat_history):
    # 并装历史会话， ChatCompletion 的 messages 部分格式
    his_msg = history_to_prompt(chat_history)
    # 放入当前用户问题
    his_msg.append({"role": "user", "content": message})
    bot_message = get_response(his_msg)
    chat_history.append((message, bot_message))
    return "", chat_history

with gr.Blocks() as block:
    chatbot = gr.Chatbot(height=480)
    msg = gr.Textbox(label="Prompt")
    btn = gr.Button("Submit")
    clear = gr.ClearButton(components=[msg, chatbot], value="Clear console")

    btn.click(respond, inputs=[msg, chatbot], outputs=[msg, chatbot])
    msg.submit(respond, inputs=[msg, chatbot], outputs=[msg, chatbot])

gr.close_all()
block.launch(share=True)