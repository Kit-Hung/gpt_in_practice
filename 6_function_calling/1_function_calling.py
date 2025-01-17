import json

from openai import OpenAI

client = OpenAI()


def get_current_cluster_state(cluster_name):
    print(f"cluster: {cluster_name}")
    return """ERROR: Failed to pull image "dsp:latest" """


funcs = {"get_current_cluster_state": get_current_cluster_state}


def run(inputs):
    msg = [{"role": "user", "content": inputs}]
    ret = run_conversation(msg)
    return ret.content


def run_conversation(msg):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=msg,
        functions=[
            {
                "name": "get_current_cluster_state",
                "description": "Get the current state in a given cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_name": {
                            "type": "string",
                            "description": "The name of the cluster."
                        },
                    },
                    "required": ["cluster_name"],
                }
            }
        ],
        # function_call="auto",
    )

    response_message = response.choices[0].message
    function_call = response_message.function_call

    # 如果不需要用 function ， 则直接返回结果
    if not function_call:
        return response_message

    # 获取调用方法
    function_name = function_call.name
    function_to_call = funcs[function_name]
    function_args = json.loads(response_message.function_call.arguments)
    function_response = function_to_call(**function_args)

    msg.append( # adding assistant response to messages
        {
            "role": response_message.role,
            "function_call": {
                "name": function_name,
                "arguments": response_message.function_call.arguments,
            },
            "content": None,
        }
    )

    msg.append({
        "role": "function",
        "name": function_name,
        "content": function_response,
    })
    return run_conversation(msg)


print(run("What's wrong with the cluster 'DSP'? And if there's an error, give me some suggestions."))
