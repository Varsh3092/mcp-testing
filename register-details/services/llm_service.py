import httpx

from langchain_openai import ChatOpenAI


llm_key = "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"

http_client = httpx.Client(
    verify=False
)

llm = ChatOpenAI(
    model="gpt-5",
    openai_api_key=llm_key,
    http_client=http_client
)


def explain_register(
    register_text: str
):
    prompt = f"""
You are an Embedded Register Expert.

Analyze the following register information.

Generate:

1. Register Name
2. Description
3. Offset
4. Reset Value
5. Bit Fields
6. Detailed Explanation

Register Data:

{register_text}
"""

    response = llm.invoke(prompt)

    return response.content
