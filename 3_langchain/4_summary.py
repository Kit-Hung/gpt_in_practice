from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain

from utils import util

llm = util.get_ChatOpenAI()

summarizing_prompt_template = """
Summarize the following content into a sentence less than 20 words:
---
{content}

"""

summarizing_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(summarizing_prompt_template),
    output_key="summary",
)

translating_prompt_template = """
translate "{summary}" into Chinese:

"""

translating_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(translating_prompt_template),
    output_key="translated",
)

overall_chain = SequentialChain(
    chains=[summarizing_chain, translating_chain],
    input_variables=["content"],
    output_variables=["summary", "translated"],
    verbose=True,
)

res = overall_chain(
    """
    LangChain is a framework for developing applications powered by language models. It enables applications that are:
    
    Data-aware: connect a language model to other sources of data
    Agentic: allow a language model to interact with its environment
    The main value props of LangChain are:
    
    Components: abstractions for working with language models, along with a collection of implementations for each abstraction. Components are modular and easy-to-use, whether you are using the rest of the LangChain framework or not
    Off-the-shelf chains: a structured assembly of components for accomplishing specific higher-level tasks
    Off-the-shelf chains make it easy to get started. For more complex applications and nuanced use-cases, components make it easy to customize existing chains or build new ones.
    """
)
print("summary: " + res["summary"])
print("中文： " + res["translated"])
