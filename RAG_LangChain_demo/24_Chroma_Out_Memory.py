# 使用Chrome
from langchain_community.document_loaders import CSVLoader
# from langchain_core.vectorstores import InMemoryVectorStore
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
# 创建存储对象
# store = InMemoryVectorStore(DashScopeEmbeddings())
store = Chroma(
    embedding_function=DashScopeEmbeddings(),
    persist_directory="./data/storage/chroma_db",
    collection_name="chroma_db"
)
#
# csv_loader = CSVLoader(file_path="./data/info", source_column="source", encoding="utf-8")
#
# load = csv_loader.load()
#
# # 内存存储文档
# store.add_documents(documents=load,ids=["ids"+str(i) for i in range(1,len(load)+1)])

# 内存搜索                                                            可以指定搜索源头名字
search = store.similarity_search("Python学起来很简单的", k=3,filter={"source": "黑马程序员"})

for i in search:
    print(i)
