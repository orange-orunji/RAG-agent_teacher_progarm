import time

import streamlit as sl
from knowledge_base import KnowledgeBaseService

sl.title("数据库芝士更新服务")

file_uploader = sl.file_uploader("请上传文件", type=["csv", "txt"],accept_multiple_files=False)

# 用session_state来存储KnowledgeBaseService对象实现全局统一
if "servers" not in sl.session_state:
    sl.session_state["servers"] : KnowledgeBaseService = KnowledgeBaseService()

if file_uploader is not None:
    file_name = file_uploader.name
    file_type = file_uploader.type
    size = file_uploader.size

    sl.subheader(f"文件名为:{file_name}")
    sl.write(f"文件类型为:{file_type}")
    sl.write(f"文件大小为:{size}")
    file_value = file_uploader.getvalue()
    sl.write(f"文件内容为:{file_value.decode('utf-8')}")

    with sl.spinner("thinking..."):
        time.sleep(1)
        result = sl.session_state["servers"].upload_by_str(file_value.decode("utf-8"), file_name)
        sl.success(result[0])
