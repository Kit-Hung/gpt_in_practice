"""
1.写一句中文，然后通过 API 让 GPT 输出英语译文
2.分别计算问题 1 中英语句子及对应中文译文的 token 数
"""
import os

from openai import OpenAI
import tiktoken

model = "gpt-3.5-turbo"
chinese = "你好吗？"

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_BASE_URL"),
)

response = client.chat.completions.create(
    model=model,
    temperature=0.9,
    max_tokens=2000,
    messages=[
        {"role": "system", "content": "你是一个翻译助手"},
        {"role": "user", "content": f"请把【{chinese}】翻译成英文"}
    ]
)
english = response.choices[0].message.content

encoding = tiktoken.encoding_for_model(model)
chinese_tokens = encoding.encode(chinese)
english_tokens = encoding.encode(english)
print(f"中文问题为： {chinese}, tokens: {chinese_tokens}, token count: {len(chinese_tokens)}\n")
print(f"英文译文为： {english}, tokens: {english_tokens}, token count: {len(english_tokens)}\n")
