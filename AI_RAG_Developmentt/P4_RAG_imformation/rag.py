from langchain_community.chat_models import ChatTongyi
from langchain_core.documents import Document
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.runnables import RunnablePassthrough
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
                ("human","问题:{question}")
            ]
        )
        self.chain = self.get_chain()

    def get_chain(self):
        store = self.vector_store.get_vector()

        chain = (
            {
                "question": RunnablePassthrough(),
                "content": store | self.__format_from_documents
            } | self.prompt | self.model
        )
        return chain


    @staticmethod
    def __format_from_documents(all_document : list[Document]):
        if not all_document:
            return "无相关参考资料"
        document_str = ""
        for doc in all_document:
            document_str += f"文档片段：{doc.page_content}\n"
        return document_str

if __name__ == '__main__':
    rag = RAGService()
    result = rag.chain.invoke("我的体重为135,帮我推荐尺码")
    print(result.content)