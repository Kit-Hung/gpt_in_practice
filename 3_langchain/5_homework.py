# 1.先将用户问题利用搜索引擎进行检索，然后再翻译成英文
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain
from langchain_community.chains.llm_requests import LLMRequestsChain
from langchain_core.prompts import PromptTemplate

from utils import util
llm = util.get_ChatOpenAI(model_name="gpt-4")

search_template = """Between >>> and <<< are the raw search result text from web.
          Extract the answer to the question '{query}' or say "not found" if the information is not contained.
          Use the format
          Extracted:<answer or "not found">
          >>> {requests_result} <<<
          Extracted:"""

search_prompt = PromptTemplate(
    template=search_template,
    input_variables=["query", "requests_result"],
)

search_chain = LLMRequestsChain(
    llm_chain=LLMChain(llm=llm, prompt=search_prompt),
    output_key="search_result",
)

translating_prompt_template = """
translate "{search_result}" into English:

"""

translate_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(translating_prompt_template),
    output_key="translation_result",
)

def overall(question):
    inputs = {
        "query": question,
        "url": "http://www.baidu.com/s?wd=" + question.replace(" ", "+")
    }

    overall_chain = SequentialChain(
        chains=[search_chain, translate_chain],
        input_variables=["query", "url"],
        output_variables=["search_result", "translation_result"],
        verbose=True,
    )

    res = overall_chain(inputs=inputs)
    print("search_result: " + res["search_result"])
    print("translation_result: " + res["translation_result"])

if __name__ == '__main__':
    overall("广州今天天气")