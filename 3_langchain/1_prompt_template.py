from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from utils import util

prompt_template = "What is a good name for a company that makes {product}? And only return the best one."

llm = ChatOpenAI(
    model_name=util.get_model(),
    temperature=0
)

llm_chain = PromptTemplate.from_template(prompt_template) | llm
# result = llm_chain.invoke({"product": "colorful socks"})
# print(result.content)

products = ["'cloudnative devops platform'",
            "'Noise cancellation headphone'",
            "colorful socks"]

# 使用invoke方法进行同步调用，处理数组中的每个输入
responses = [llm_chain.invoke({"product": product}) for product in products]

# 打印每个响应的内容
for response in responses:
    print(response.content)
