# 1.用 GPT 编写一个用户评语判断程序，输入用户评论，输出评论是正向的还是反向的，分别用
# Y 和 N 来表示

from utils import util

client = util.get_client()
response = client.chat.completions.create(
    model=util.get_model(),
    temperature=0,
    max_tokens=100,
    messages=[
        {"role": "system",
         "content": """你是一个用户评语小助手，判断用户评论，如果是正向评论输出 "Y"，如果是反向评论输出 "N" """},
        # {"role": "user", "content": "这本书真有趣"},
        {"role": "user", "content": "这个人好无聊"},
    ]
)

print(response.choices[0].message.content)
