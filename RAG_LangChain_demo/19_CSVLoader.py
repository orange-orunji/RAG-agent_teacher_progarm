# CSV读取器
from langchain_community.document_loaders import CSVLoader

csv_loader = CSVLoader(
    file_path="./data/stu.csv",
    encoding="utf-8",
    csv_args={
        "delimiter":",",
        "quotechar":'"',
        # "filedname":["name","age","gender","hobby"]
    }

)

# 全加载
# print(csv_loader.load())

# 懒加载
for i in csv_loader.lazy_load():
    print(i)
