from langchain_community.llms.tongyi import Tongyi

# 创建模型对象
model  = Tongyi(model="qwen-max")

res = model.invoke("你是谁呀")
print(res)
