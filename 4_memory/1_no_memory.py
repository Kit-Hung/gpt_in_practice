import os
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


if __name__ == '__main__':
    print(get_response("你好，今天是周二我要去健身，我一般每周二健身，你今天干什么？"))
    print(get_response("我一般周几健身？"))
