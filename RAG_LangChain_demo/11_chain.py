# chain的使用
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi

messages = ChatPromptTemplate.from_messages(
    [('system', "你作为一名资深的backend架构师"), MessagesPlaceholder("history"),
     ('user', "请帮我用java写一个hello world程序"), ])

message =   [
        ('user',"请帮我解释redis缓存的作用"),
        ('assistant',"redis缓存的作用是存储数据，提高查询效率")
    ]

chain = messages | ChatTongyi(model="qwen-max")

for chunk in chain.stream({"history": message}):
     print(chunk.content,end="",flush=True)