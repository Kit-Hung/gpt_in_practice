# 处理错误返回
from utils import util

system_prompt = """  You are a software engineer, you can write a SQL string as the answer according to the user request 
               The user's requirement is based on the given tables:
                  table “students“ with the columns [id, name, course_id, score];
                  table "courses" with the columns [id, name]."""

system_prompt_with_negative = """  
You are a software engineer, you can write a SQL string as the answer according to the user request.
Also, when you cannot create the SQL query for the user's request based on the given tables, please, only return "invalid request"
               The user's requirement is based on the given tables:
                  table “students“ with the columns [id, name, course_id, score];
                  table "courses" with the columns [id, name]."""

# prompt = system_prompt
prompt = system_prompt_with_negative

client = util.get_client()
response = client.chat.completions.create(
    model=util.get_model(),
    temperature=0,
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": "列出年龄大于13的学生"}
    ],
    max_tokens=500,
)
print(response.choices[0].message.content)
