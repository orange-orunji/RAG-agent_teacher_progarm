# 通用模板提示词
from langchain_community.llms.tongyi import Tongyi
# 导入通用模板
from langchain_core.prompts import PromptTemplate
model  = Tongyi(model = "qwen-max")

prompt = PromptTemplate.from_template(
  "我的邻居姓{lastname},是一个{gender},请帮他起个名字"
)
# 调用.fromat方法注入信息
# chain = prompt.format(lastname='张',gender='女生')
# m = model.invo(chain)
# print(m,end="",flush=True)

# 利用chain链对象来添加执行链条
chain = prompt | model
c = chain.invoke(input={"lastname":"张","gender":"女生"})
print(c,end="",flush=True)

