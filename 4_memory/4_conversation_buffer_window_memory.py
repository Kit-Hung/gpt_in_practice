import gradio as gr

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, trim_messages
from utils import util

model = "gpt-3.5-turbo"
llm = ChatOpenAI(
    model_name=model,
    temperature=0.3,
    max_tokens=1000,
    streaming=True,
)


def get_response(messages):
    print("----------------")
    selected_messages = trim_messages(
        messages=messages,
        token_counter=llm,
        max_tokens=1000,
        start_on="human",
        include_system=True,
        strategy="last",
    )
    print(selected_messages)
    print("----------------")
    response = llm.invoke(selected_messages)

    selected_messages.append(response)
    return selected_messages


def respond(message, chat_history):
    messages = util.change_to_message(chat_history)
    messages.append(HumanMessage(message))

    bot_messages = get_response(messages)
    chat_histories = util.change_to_gradio_message(bot_messages)
    return "", chat_histories


with gr.Blocks() as blocks:
    chatbot = gr.Chatbot(height=300, type="messages")
    msg = gr.Textbox(label="Prompt")
    btn = gr.Button("Submit")
    clear = gr.ClearButton(components=[msg, chatbot], value="Clear console")

    btn.click(respond, inputs=[msg, chatbot], outputs=[msg, chatbot])
    msg.submit(respond, inputs=[msg, chatbot], outputs=[msg, chatbot])

gr.close_all()
blocks.launch(share=True)
