# 意图识别
from utils import util

client = util.get_client()
response = client.chat.completions.create(
    model=util.get_model(),
    temperature=0,
    messages=[
        {"role": "system", "content": "Recognize the intent from the user's input"},
        # {"role": "user", "content": "订明天早5点北京到上海的飞机"}
        {"role": "user", "content": "提醒我明早8点有会议"}
    ]
)
print(response.choices[0].message.content)
