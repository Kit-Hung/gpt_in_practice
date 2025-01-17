import gradio as gr
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain

model = "gpt-3.5-turbo"
llm = ChatOpenAI(
    model_name=model,
    temperature=0.3,
    max_tokens=1000,
    streaming=True,
)

memory = ConversationBufferWindowMemory(k=10)


def get_response(inputs):
    print("----------------")
    print(memory.load_memory_variables({}))
    print("----------------")
    conversation_with_memory = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=False,
    )
    return conversation_with_memory.predict(input=inputs)


def respond(message, chat_history):
    bot_message = get_response(message)
    chat_history.append((message, bot_message))
    return "", chat_history


with gr.Blocks() as blocks:
    chatbot = gr.Chatbot(height=300, type="tuples")
    msg = gr.Textbox(label="Prompt")
    btn = gr.Button("Submit")
    clear = gr.ClearButton(components=[msg, chatbot], value="Clear console")

    btn.click(respond, inputs=[msg, chatbot], outputs=[msg, chatbot])
    msg.submit(respond, inputs=[msg, chatbot], outputs=[msg, chatbot])

gr.close_all()
blocks.launch(share=True)
