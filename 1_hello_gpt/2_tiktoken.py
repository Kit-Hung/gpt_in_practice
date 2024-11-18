import tiktoken

model = "gpt-3.5-turbo"
encoding = tiktoken.encoding_for_model(model)
chinese = "在未来还没有到来的时候，总要有人把它创造出来，那个人应该是我们。"
tokens = encoding.encode(chinese)
print(tokens)

num_of_token_in_chinese = len(tokens)
print(f"chinese: {chinese}; {num_of_token_in_chinese} tokens\n")
