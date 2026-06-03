
import streamlit as sl

sl.title("文件上传")

file_uploader = sl.file_uploader("请上传文件", type=["csv", "txt"],accept_multiple_files=False)

if file_uploader is not None:
    file_name = file_uploader.name
    file_type = file_uploader.type
    size = file_uploader.size

    sl.subheader(f"文件名为:{file_name}")
    sl.write(f"文件类型为:{file_type}")
    sl.write(f"文件大小为:{size}")
    sl.write(f"文件内容为:{file_uploader.getvalue().decode('utf-8')}")
