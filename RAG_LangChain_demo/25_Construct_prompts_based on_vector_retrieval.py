# 基于向量检索构造提示词

from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore

store = InMemoryVectorStore(DashScopeEmbeddings(model="text-embedding-v4"))

store.add_texts(["减肥就是药少吃多练","在减脂期吃东西很重要，清淡少油控制卡路里摄入并运动起来","跑步是很好的运动"])

input_message = "要怎么减肥"

content = store.similarity_search(input_message,k=2)
information_list="["
for i in content:
    information_list+=i.page_content+","
information_list+="]"

template = ChatPromptTemplate(
    messages=[
        {"role": "system", "content": "基于以下信息回答问题{information_list}"},
        {"role": "user", "content": "{input_message}"}
    ])

model = ChatTongyi(model="qwen-max")

def print_prompt(all_prompt):
    for prompt in all_prompt:
        print(prompt)
    return all_prompt

chain = template | print_prompt | model


for chunk in chain.stream(input={"input_message":input_message,"information_list":information_list}):
    print(chunk.content,end="",flush=True)
