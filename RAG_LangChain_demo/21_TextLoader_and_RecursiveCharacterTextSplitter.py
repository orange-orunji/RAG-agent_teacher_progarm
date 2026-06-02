# RecursiveCharacterTextSplitter迭代切割器和TextLoader文本加载的用法
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 文本读取器
loader = TextLoader("data/Python", encoding="utf-8")

# 分割器
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=10, separators=["\n\n", "\n", "\t", " "],
                                          length_function=len)

load = loader.lazy_load()

for split_document in splitter.split_documents(load):
    print("---------------------------------------------------------------------------------------------------------")
    print(split_document)
    print("---------------------------------------------------------------------------------------------------------")


loader = TextLoader("data/Python", encoding="utf-8")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,  # 分块大小
    chunk_overlap=50,  # 重叠长度
    length_function=len,  # 长度函数
    separators=["\n\n", "\n", "\t", " "]  # 分隔符
)

document = loader.load()

for chunk in splitter.split_documents(document):
    print("="*20)
    print(chunk)
    print("="*20)

