"""流式输出"""
from langchain_community.llms.tongyi import Tongyi

model  = Tongyi(model="qwen-max")
res = model.stream(input="什么是java")
for chunk in  res:
  print(chunk,end='',flush=True)