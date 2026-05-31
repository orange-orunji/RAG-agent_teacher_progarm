# fewshot提示词模板
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_community.llms.tongyi import Tongyi

example_prompt = PromptTemplate.from_template("单词:{word},反义词:{antoword}")

example_data = [
  {"word":"上","antoword":"下"},
  {"word":"男","antoword":"女"}
]

fewshot = FewShotPromptTemplate(
  example_prompt=example_prompt,
  examples=example_data,
  prefix = "告知我词语的翻译成，根据以下提供的文本案例：",
  suffix = "基于前面的案例告知我{word}的反义词",
  input_variables=['word']
  )
  
text = fewshot.invoke(input={"word":"左"}).to_string()

model = Tongyi(model="qwen-max")
print(model.invoke(input=text))



# example_prompt = PromptTemplate.from_template("单词:{word},反义词:{anword}")
# examples=[
#   {"word":"上","anword":"下"}, 
#   {"word":"前","anword":"后"} 
# ]
# few_shot_prompt_template = FewShotPromptTemplate(
#   example_prompt=example_prompt,
#   examples=examples,
#   prefix = "告知我词语的翻译成，根据以下提供的文本案例：",
#   suffix = "基于前面的案例告知我{word}的反义词",
#   input_variables=['word']
# )
# text = few_shot_prompt_template.invoke(input={"word":"左"}).to_string()
# model = Tongyi(model="qwen-max")
# print(model.invoke(input=text))

