# 基于向量检索构造提示词

from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.vectorstores import InMemoryVectorStore

store = InMemoryVectorStore(DashScopeEmbeddings(model="text-embedding-v4"))

store.add_texts(["减肥就是药少吃多练","在减脂期吃东西很重要，清淡少油控制卡路里摄入并运动起来","跑步是很好的运动"])

input_message = "要怎么减肥"

# content = store.similarity_search(input_message,k=2)
# information_list="["
# for i in content:
#     information_list+=i.page_content+","
# information_list+="]"
content = store.as_retriever(search_kwargs={"k":2})

template = ChatPromptTemplate(
    messages=[
        {"role": "system", "content": "基于以下信息回答问题{information_list}"},
        {"role": "user", "content": "{input_message}"}
    ])

model = ChatTongyi(model="qwen-max")

def print_prompt(all_prompt):
    if not all_prompt:
        return "暂无参考数据"
    for i in all_prompt:
        print(i)
    return all_prompt

def parse_content(docs):
    if not docs:
        return "暂无参考数据"
    return "\n".join([doc.page_content for doc in docs])



chain = {"input_message": RunnablePassthrough(),"information_list":content | parse_content} | template | print_prompt | model

print(chain.invoke(input_message).content)

