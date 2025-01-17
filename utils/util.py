import os
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from gradio.components.chatbot import Message

ChatBot_Role_User = "user"
ChatBot_Role_Assistant = "assistant"


def get_model(model="gpt-3.5-turbo") -> str:
    return model


def get_client() -> OpenAI:
    return OpenAI(
        api_key=os.environ["OPENAI_API_KEY"],
        base_url=os.environ["OPENAI_BASE_URL"],
    )


def get_ChatOpenAI(model_name=get_model(), temperature=0) -> ChatOpenAI:
    return ChatOpenAI(
        model_name=model_name,
        temperature=temperature,
    )


def change_to_message(chat_histories: dict) -> list[BaseMessage]:
    messages = []
    for chat_history in chat_histories:
        if chat_history is None:
            continue

        role = chat_history["role"]
        content = chat_history["content"]
        if role == ChatBot_Role_User:
            messages.append(HumanMessage(content))
        elif role == ChatBot_Role_Assistant:
            messages.append(AIMessage(content))

    return messages


def change_to_gradio_message(messages: BaseMessage) -> list[Message]:
    chat_histories = []

    for message in messages:
        if message is None:
            continue

        if isinstance(message, HumanMessage):
            chat_histories.append(Message(role=ChatBot_Role_User, content=message.content))
        elif isinstance(message, AIMessage):
            chat_histories.append(Message(role=ChatBot_Role_Assistant, content=message.content))

    return chat_histories
