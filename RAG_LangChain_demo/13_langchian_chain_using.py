# langchain中chain是将内容拼接成一个RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

tongyi = Tongyi(model="qwen-max")
template = PromptTemplate.from_template("我的邻居姓{lastname},是一个{gender},请帮他起个名字")

chain = template | tongyi
print(chain,type(chain))

# first=PromptTemplate(input_variables=['gender', 'lastname'], input_types={}, partial_variables={}, template='我的邻居姓{lastname},是一个{gender},请帮他起个名字') middle=[] last=Tongyi(client=<class 'dashscope.aigc.generation.Generation'>, model_name='qwen-max', model_kwargs={})
# <class 'langchain_core.runnables.base.RunnableSequence'>
 