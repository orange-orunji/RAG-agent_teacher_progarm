# 定义向量检索对象供外部使用
from langchain_chroma import Chroma
import config_data as config

class VectorStoreServer:
    def __init__(self,embedding_model):
        self.embedding = embedding_model

        self.chroma = Chroma(
            embedding_function=self.embedding,
            persist_directory=config.chroma_path,
            collection_name=config.chroma_name
        )
    def get_vector(self):
        # 获取向量检索器，方便后续加入链
        return self.chroma.as_retriever(search_kwargs={"k":config.vector_num})

if __name__ == '__main__':
    from langchain_community.embeddings import DashScopeEmbeddings
    vector_store = VectorStoreServer(DashScopeEmbeddings(model="text-embedding-v1"))
    print(vector_store.get_vector().invoke("我的体重为135,帮我推荐尺码"))
