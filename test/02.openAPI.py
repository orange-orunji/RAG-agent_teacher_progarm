from openai import OpenAI
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
    {'role':"user",'content':"redis中分布式锁怎么实现"}
  ]
)
# 3.输出返回结果
print(c.choices[0].message.content)