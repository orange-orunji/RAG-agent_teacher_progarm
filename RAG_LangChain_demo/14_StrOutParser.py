# 字符串输出解释器StrOutParser的用法
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

parser = StrOutputParser()
model = ChatTongyi(model="qwen-max")
prompt = PromptTemplate.from_template("请将{text}翻译成英文")
chain = prompt | model | parser |  model
invoke = chain.invoke(input={"text": "你好"})
print(invoke.content)