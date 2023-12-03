import json
import os

json_jp = "json_jp"
json_cn = "json_cn"
output_file = "output.json"  # 输出 JSON 文件名

new_data = {}  # 存储修改后的新数据

# 遍历json_jp的所有文件
for filename in os.listdir(json_jp):
    if filename.endswith(".json"):
        input_file = os.path.join(json_jp, filename)

        # 读取json文件
        with open(input_file, "r", encoding="utf-8") as fp:
            data = json.load(fp)

        # 从json_cn中查找匹配的json文件
        match_file = os.path.join(json_cn, filename)
        with open(match_file, "r", encoding="utf-8") as fp:
            match_data = json.load(fp)

        # 遍历每个字典项
        for item in data:
            name1 = item.get("name")  # 使用字典的 get 方法，如果 name 不存在则返回 None
            message1 = item.get("message")  # 使用字典的 get 方法，如果 message 不存在则返回 None

            match_item = match_data.pop(0)
            name2 = match_item.get("name")  # 使用字典的 get 方法，如果 name 不存在则返回 None
            message2 = match_item.get("message")  # 使用字典的 get 方法，如果 message 不存在则返回 None

            if name1 and name2:
                script = name1 + message1
                translate = name2 + message2
            elif message1 and message2:
                script = message1
                translate = message2

            new_data[script] = translate

# 写入新的 JSON 文件
with open(output_file, "w", encoding="utf-8") as fp:
    json.dump(new_data, fp, ensure_ascii=False, indent=4)
