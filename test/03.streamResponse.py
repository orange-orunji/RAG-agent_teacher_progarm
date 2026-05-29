import sys
from openai import OpenAI

sys.stdout.reconfigure(encoding="utf-8")
# 1.获取client客户端对象,OenAI对象
client : OpenAI = OpenAI(
  base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
# 2.创建模型
c = client.chat.completions.create(
  model="qwen-plus",
  messages=[
    {'role':"system",'content':'你是一名资深的java专家'},
    {'role':"assistant",'content':"好的,我是一名资深的java专家,回答不说废话"},
    {'role':"user",'content':"redis是什么"}
  ],
  stream=True
)
# 3.输出返回结果
for chunk in c:
  print(chunk.choices[0].delta.content,end="",flush=True)