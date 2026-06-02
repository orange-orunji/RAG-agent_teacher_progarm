# 长期会话记忆实现 使用本地文件读取存储数据来实现
import json
import os

from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage, messages_from_dict, HumanMessage, message_to_dict


class FileChatHistory(BaseChatMessageHistory):
    def __init__(self,session_id,storage_path):
        self.session_id = session_id
        self.storage_path = storage_path

        # 创建文件夹以确保文件存在
        os.makedirs(self.storage_path,exist_ok=True)

        self.file_path = os.path.join(self.storage_path,self.session_id)

    def add_message(self, messages: BaseMessage) -> None:
        before_messages = self.messages
        all_messages = before_messages.copy()
        all_messages.append(messages)
        """
        将数据同步写入到本地文件中
        类对象写入文件  ->  一堆二进制
        为了方便，可以将BaseMessage消息转为字典(借助json模块以json字符串写入文件)
        官方message_to_dic:单个消息对象(BaseMessage类示例)->字典
        """
        all_messages = [message_to_dict(message) for message in all_messages]
        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump(all_messages,f)


    @property
    def messages(self) -> list[BaseMessage]:
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path,"r",encoding="utf-8") as f:
                load_message = json.load(f)
            return messages_from_dict(load_message)
        except FileExistsError:
            return []
    def clear(self) -> None:
        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump([],f)
if __name__ == '__main__':
    history = FileChatHistory("test", "./storage")
    history.add_message(HumanMessage(content="hello"))
    print(history.messages.__str__())
    history.clear()
