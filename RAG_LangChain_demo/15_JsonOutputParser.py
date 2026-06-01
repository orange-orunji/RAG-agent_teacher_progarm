"""
前面的需求去构建多模型链做法不够标准,
因为:上一个模型的输出没有被处理就输出给了下一个模型

正常情况下应该有的处理逻辑                             1            1
 invoke | stream 初始输入 -> 提示词模板 -> 模型 -> 数据处理 -> 提示词模板 -> 解析器 -> 结果
 """
from langchain_core.prompts import  PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi

model = ChatTongyi(model="qwen-max")
first_prompt = PromptTemplate.from_template("我的邻居姓{lastname},最近生了个{gender},请帮我想一个名字，要求返回为json格式"
                                      "内嵌为字典类型，key值为name,value值为生成的姓名，不做额外的思考输出,仅回复对应的字典规范"
                                      "请严格准许次规范")

second_prompt = PromptTemplate.from_template("请帮我解析名字{name}")
parser = JsonOutputParser()
output_parser = StrOutputParser()

#  invoke | stream 初始输入 -> 提示词模板 -> 模型 -> 数据处理 -> 提示词模板 -> 解析器 -> 结果
stream = first_prompt | model | parser | second_prompt | model | output_parser

for chunk in stream.invoke(input={"lastname":"张","gender":"女儿"}):
  print(chunk,end="",flush=True)
