import time

import streamlit as st

import config_data as config
from rag import RAGService

# 标题
st.title("智能助手")
st.divider() #分隔符
session_state = st.session_state

if "rag" not in session_state:
    session_state["rag"] = RAGService()

if "message" not in session_state:
    session_state["message"] = [{"role": "assistant", "content": "欢迎来到智能助手,请问有什么可以帮助你"}]

for message in session_state["message"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])


prompt = st.chat_input("question", key="question")

configss = {"configurable": {"session_id": config.session_id}}
if prompt:
    st.chat_message("user").write(prompt)
    session_state["message"].append({"role": "user", "content": prompt})

    message_list = []
    #
    with st.chat_message("assistant"):
        def print_prompt(full_prompt):
            for chunk in full_prompt:
                message_list.append(chunk.content)
                yield chunk.content
        stream = session_state["rag"].stream_chain.stream(input={"input":prompt})
        st.write_stream(print_prompt(stream))
    session_state["message"].append({"role": "assistant", "content": "".join(message_list)})




