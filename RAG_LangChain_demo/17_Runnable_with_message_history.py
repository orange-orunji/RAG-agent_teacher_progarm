"""
RunnableWithMessageHistory的使用来短期暂时存储历史记录
"""
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate

model = ChatTongyi(model="qwen-max")
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', "你是一个问答助手,请严格准时简洁易懂的回答方式,不输出多余赘述内容"),
        ("user","历史记录为{history},用户提问的内容为{input}]")
    ]
)

base_chain = prompt  | model

# 定义一个获取历史记录的函数
# 定义一个字典来存储历史记录的id
session_id = {}
def get_history(id):
    if id not in session_id:
        session_id[id] = InMemoryChatMessageHistory()
    return session_id[id]


with_message_history = RunnableWithMessageHistory(base_chain, get_history, input_messages_key="input",
                                     history_messages_key="history")

if __name__ == '__main__':
    session_config = {
        "configurable":{
            "session_id": "user_0001"
        }
    }

    print("第一次提问",with_message_history.invoke({"input":"小明有一只猫"},session_config).content)
    print("第二次提问",with_message_history.invoke({"input":"小刚有三只狗"},session_config).content)
    print("第三次提问",with_message_history.invoke({"input":"请问有几只宠物"},session_config).content)
