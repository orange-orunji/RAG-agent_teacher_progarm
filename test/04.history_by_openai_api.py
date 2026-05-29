import sys
from openai import OpenAI

sys.stdout.reconfigure(encoding="utf-8")
# 1.获取client客户端对象,OenAI对象
client : OpenAI = OpenAI(
  api_key="sk-1a60e37ca4434f41ba71d8e11d0b4e60",
  base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
# 2.创建模型
c = client.chat.completions.create(
  model="qwen-plus",
  messages=[
    {'role':"user",'content':"我养了两只猫"},
    {'role':"assistant",'content':"好的"},  
    {'role':"user",'content':"我养了三只狗"},
    {'role':"assistant",'content':"好的"},
    {'role':"user",'content':"我养了几只宠物呀,分别有什么"}

  ],
  stream=True
)
# 3.输出返回结果
for chunk in c:
  print(chunk.choices[0].delta.content,end="",flush=True)