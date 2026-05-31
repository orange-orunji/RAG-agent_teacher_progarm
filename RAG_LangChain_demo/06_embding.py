# 嵌入模型调用
from langchain_community.embeddings import DashScopeEmbeddings

# 默认使用text。。。来做
model = DashScopeEmbeddings()

print(model.embed_query("我喜欢你"))
print(model.embed_documents(["我喜欢你","我稀罕你","我爱你"]))