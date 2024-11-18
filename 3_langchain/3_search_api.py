import os

os.environ["SERPER_API_KEY"] = ""

# https://serper.dev

from langchain.utilities import GoogleSerperAPIWrapper


def query_web(question):
    search = GoogleSerperAPIWrapper()
    return search.run(question)


if __name__ == '__main__':
    query_web("今天北京天气？")
