"""
 invoke和format的使用
"""
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate,FewShotPromptTemplate

template = PromptTemplate.from_template("请将{word}翻译成英文")

# format方法
prompt = template.format(word="左")
print(prompt,type(prompt))


# invoke方法
invoke = template.invoke(input={"word": "左"})
print(invoke.to_string(),type(invoke))
