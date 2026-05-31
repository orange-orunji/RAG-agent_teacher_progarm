# langchain调用语言聊天模型
from email import message
from httpx import stream
from langchain_community.chat_models import ChatTongyi 
from langchain.messages import AIMessage,HumanMessage,SystemMessage

model = ChatTongyi(model="qwen3-max")

messages = [
  SystemMessage(content="你是杜甫"),
  HumanMessage(content="帮我写一首唐诗"),
  AIMessage(content="锄禾日当午,汗滴禾下土.谁知盘中餐,粒粒皆辛苦."),
  HumanMessage(content="帮我根据以上格式帮我写一首唐诗")
]

res = model.stream(input=messages)
for chunk in res:
  print(chunk.content,flush=True,end="")