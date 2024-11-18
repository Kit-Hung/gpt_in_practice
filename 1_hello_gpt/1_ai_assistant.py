import os

from openai import OpenAI

model = "gpt-3.5-turbo"
reply_count = 3

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
    base_url=os.environ['OPENAI_BASE_URL']
)

response = client.chat.completions.create(
    model=model,
    # 取值在 0~2 之间，越小输出越稳定，越大输出越具有随机性
    temperature=0.9,
    # 内容产生的最大长度限制
    # 太小会截断，finish_reason='length'
    # 正常生成，finish_reason='stop'
    # max_token 用于限制生成内容的最大 token 数
    # 另外，提示词的 token 数加上 max_tokens 的值不能大于模型支持的内容长度
    max_tokens=10,
    # 回复的个数
    # n=reply_count,
    messages=[
        # system: 用于在这个会话中设置 AI 助手的个性或提供有关其在整个对话过程中应如何表现的具体说明
        {"role": "system", "content": "你是一个 AI 助理"},
        # user: 用于向 AI 助理提出需求
        {"role": "user", "content": "你好！你叫什么名字？"}
    ]
)
print(response)
# print(response.choices[0].message.content)
print([choice.message.content for choice in response.choices])
