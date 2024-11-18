# 生成 sql
from utils import util

system_prompt = """ You are a software engineer, you can write a SQL string as the answer according to the user request 
               The user's requirement is based on the given tables:
                  table “students“ with the columns [id, name, course_id, score];
                  table "courses" with the columns [id, name].
"""

client = util.get_client()
response = client.chat.completions.create(
    model=util.get_model(),
    temperature=0,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "列出英语课程成绩大于80分的学生，返回结果只包含 SQL"}
    ],
    max_tokens=500,
)
print(response.choices[0].message.content)
