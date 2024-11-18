from langchain.chains.llm import LLMChain
from langchain_community.chains.llm_requests import LLMRequestsChain
from langchain_core.prompts import PromptTemplate

from utils import util

llm = util.get_ChatOpenAI(model_name="gpt-4")


def query_baidu(question):
    template = """Between >>> and <<< are the raw search result text from web.
          Extract the answer to the question '{query}' or say "not found" if the information is not contained.
          Use the format
          Extracted:<answer or "not found">
          >>> {requests_result} <<<
          Extracted:"""

    prompt = PromptTemplate(
        template=template,
        input_variables=["query", "question"],
    )

    inputs = {
        "query": question,
        "url": "http://www.baidu.com/s?wd=" + question.replace(" ", "+")
    }

    llm_chain = prompt | llm
    print(type(llm_chain))
    request_chain = LLMRequestsChain(
        llm_chain=LLMChain(llm=llm, prompt=prompt),
        output_key="query_info",
        verbose=True,
    )
    res = request_chain.invoke(inputs)
    return res


if __name__ == '__main__':
    print(query_baidu("广州今天天气？"))
