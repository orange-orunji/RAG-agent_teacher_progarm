# 使用InMemoryVectorStore存储信息
from langchain_community.document_loaders import CSVLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings


message_history = InMemoryVectorStore(DashScopeEmbeddings())

loader = CSVLoader(file_path="./data/info", encoding="utf-8", source_column="source")

document = loader.load()



message_history.add_documents(
    documents=document,
    ids=["ids"+str(i) for i in range(len(document))]
)

message_history.delete(["ids1","ids2"])

print(message_history.get_by_ids("ids5"))

search = message_history.similarity_search("股市", k=3)

for i in search:
    print(i)


