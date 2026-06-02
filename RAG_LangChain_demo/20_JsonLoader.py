# JsonLoader来对json文件进行读取,并用jq来对scheme语法来进行获取
import jq

from langchain_community.document_loaders import JSONLoader
"""
    jq解析语法
    .表示根,[]表示数组
    .name表示从根去name的值
    .hobby[1]从数组中获取元素
    .[]将数组中的每个字典(json对象)都取到
    .[].name
"""
json_loader = JSONLoader(
    file_path="./data/stus.json",
    jq_schema=".[].other[1]",
    text_content=False,
    # json_lines=True
)

for e in json_loader.lazy_load():
    print(e)
