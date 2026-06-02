# pyPDF来获取PDF的信息
from langchain_community.document_loaders import  PyPDFLoader

pdf_loader = PyPDFLoader(file_path="./data/pdf.pdf",
                         mode="single",#可选参数默认为page分页读取,可设置为single按单页读取
                         # password="123456",可选pdf的密码输入项
                         )

count = 0
for i in pdf_loader.load():
    print(i)
    count+=1
    print("-"*20,count)
