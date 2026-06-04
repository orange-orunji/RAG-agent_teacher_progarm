# base5存储相关方法和函数
import hashlib
import os.path

import config_data as config
from datetime import datetime
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


def check_md5(md5_file_path: str,md5_value: str):
    """检测文件md5是否存在,不存在则创建文件并返回false,成功返回True"""
    if not os.path.exists(md5_file_path):
        with open(md5_file_path, "w", encoding="utf-8"):
            pass
        return False
    else:
        t = open(md5_file_path, "r", encoding="utf-8")
        for i in t.readlines():
            if i.strip()==md5_value:
                return True
        else:
            return  False

def save_md5(md5_file_path : str,md5_value : str):
    """保存文件md5"""
    with open(md5_file_path, "a", encoding="utf-8") as f:
        f.write(md5_value+"\n")


def get_string_md5(input_str: str, encoding ="utf-8"):
    # 转成对应字符
    str_bytes = input_str.encode(encoding)

    # 转成md5
    md5_hash = hashlib.md5()
    md5_hash.update(str_bytes)
    return md5_hash.hexdigest()

class KnowledgeBaseService:
    def __init__(self):
        self.chroma = Chroma(
            embedding_function=DashScopeEmbeddings(),
            persist_directory=config.chroma_path,
            collection_name=config.chroma_name
        )
        self.spliter = RecursiveCharacterTextSplitter(
            chunk_size=config.spliter_size,
            chunk_overlap=config.spliter_overlap,
            separators=config.separators
        )

    def upload_by_str(self,data : str,filename):

        # 获得当前数据的md5值
        md_5_value = get_string_md5(data)
        if check_md5(config.md5_path, md_5_value):
            return ["[Pass]数据上传失败,该数据已存在"]

        # 判断文件大小是否需要分割
        if len(data) > config.spliter_max_chunk_size:
            self_spliter_split_text: list = self.spliter.split_text(data)
        else:
            self_spliter_split_text = [data]

        message = {
            "source": filename,
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operator": "orunji"
        }

        self.chroma.add_texts(self_spliter_split_text,metadatas=[message for _ in range(len(self_spliter_split_text))])
        save_md5(config.md5_path,md_5_value)
        return ["[Success]数据上传成功"]

if __name__ == '__main__':
    # print(get_string_md5("周杰伦"))
    # print(get_string_md5("周杰伦"))
    # print(get_string_md5("周杰伦1"))

    # save_md5(md5_path, get_string_md5("周杰伦"))

    print(check_md5(config.md5_path, get_string_md5("周杰伦")))