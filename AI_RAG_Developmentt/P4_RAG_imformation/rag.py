from operator import itemgetter

from langchain_community.chat_models import ChatTongyi
from langchain_core.documents import Document
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain_core.runnables.history import RunnableWithMessageHistory
from file_history_store import get_history
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
import os

import config_data as config
from AI_RAG_Developmentt.P4_RAG_imformation.vector_stores import VectorStoreServer


class RAGService:
    def __init__(self):
        self.model = ChatTongyi(model=config.chat_model)
        
        self.embedding = DashScopeEmbeddings(
            dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")
        )
        
        self.vector_store = VectorStoreServer(embedding_model=self.embedding)

        self.prompt = ChatPromptTemplate.from_messages(
            messages=[
                ("system","以提供的已知参考资料为主,"
                 "简洁和专业的回答用户问题，参考资料:{content}"),
                ("system","并且更根据历史信息来回答"),
                MessagesPlaceholder("history"),
                ("human","问题:{input}")
            ]
        )
        self.chain = self.get_chain()



    def get_chain(self):
        store = self.vector_store.get_vector()

        def temp1(temp_dict):
            return temp_dict["input"]
        def temp2(temp_dict):
            new_dict = {"input": temp_dict["input"]["input"], "history": temp_dict["input"].get("history", []), "content": temp_dict["content"]}
            return new_dict
        chain = (
            {
                "input": RunnablePassthrough(),
                "content": RunnableLambda(temp1)  | store | self.__format_from_documents
            } | RunnableLambda(temp2) | self.prompt | RunnableLambda(print_prompt) | self.model
        )



        conversation_chain = RunnableWithMessageHistory(
            chain,
            get_history,
            input_messages_key="input",
            history_messages_key="history"
        )
        return conversation_chain



    @staticmethod
    def __format_from_documents(all_document : list[Document]):
        if not all_document:
            return "无相关参考资料"
        document_str = ""
        for doc in all_document:
            document_str += f"文档片段：{doc.page_content}\n"
        return document_str

def print_prompt(full_prompt):
    print("="*20,full_prompt.to_string(),"="*20)
    return full_prompt

if __name__ == '__main__':
    configration = {
        "configurable":{
            "session_id": "user_0001"
        }
    }
    result = RAGService().chain.invoke({"input":"我的身高为174,帮我推荐尺码"},config=configration)
    print(result.content)