import os
from openai import OpenAI
from langchain_openai import ChatOpenAI

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