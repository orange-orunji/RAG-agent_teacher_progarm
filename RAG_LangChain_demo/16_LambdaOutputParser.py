"""想要在链中加入自定义函数可以选择:
1.将函数封装入RunnableLambda类对象,其是Runnable接口示例,可以直接入链
2.直接将函数入链,函数会自动转换为RunnableLambda对象
"""
from langchain_core.runnables import RunnableLambda
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate

model = ChatTongyi(model="qwen-max")
first_prompt = PromptTemplate.from_template("我的邻居姓{lastname},最近生了个{gender},请帮我想一个名字，并且只返回名字不返回别的内容,请严格遵守")
second_prompt = PromptTemplate.from_template("请将{name}进行解析")

# 定义Runnable对AImessage进行解析
# runnable_lambda = RunnableLambda(lambda ai_msg: {"name": ai_msg.content})

chain = first_prompt | model |( lambda ai_msg: {"name": ai_msg.content} )| second_prompt | model

stream = chain.stream(input={"lastname": "张", "gender": "女儿"})

for chunk in stream:
    print(chunk.content,end="",flush=True)

