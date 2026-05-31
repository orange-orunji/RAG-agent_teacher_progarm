# ChatPromptTemplate的使用方法
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi

messages = ChatPromptTemplate.from_messages(
    [('system', "你作为一名资深的backend架构师"), MessagesPlaceholder("history"),
     ('user', "请帮我用java写一个hello world程序"), ])

message =   [
        ('user',"请帮我解释redis缓存的作用"),
        ('assistant',"redis缓存的作用是存储数据，提高查询效率")
    ]

invoke = messages.invoke({"history": message})
true__invoke = ChatTongyi(model="qwen-max", streaming=True).invoke(invoke.to_string())
print(true__invoke.content,type(true__invoke))
#
# messages = ChatPromptTemplate.from_messages(
#     [('system', "你是一名资深的后端架构师"), MessagesPlaceholder("history"), ('user', "请帮我用java写一个hello world程序"), ])
#
# history_data=[('user',"请帮我解释redis缓存的作用"),
#     ('assistant',"redis缓存的作用是存储数据，提高查询效率")
# ]
#
# question = messages.invoke({"history": history_data}).to_string()
#
# tongyi = ChatTongyi(model="qwen-max",streaming=True)
#
# invoke = tongyi.invoke(question)
# print(invoke.content,type(invoke))