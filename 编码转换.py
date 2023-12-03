import json
import codecs
import os

unsupported_chars = []
encode = 'gbk'
encoder = codecs.getencoder(encode)
input_folder = "json"

# 打开 JSON 文件并加载数据
for filename in os.listdir(input_folder):
    if filename.endswith(".json"):
        input_path = os.path.join(input_folder, filename)
        # 读取 JSON 文件
        with open(input_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        # 遍历 JSON 数据中的每个键值对
        for item in data:
            # 检查键值对的值是否为字符串类型
            message = item.get('message')
            name = item.get('name')
            if name:
                for char in name:
                    try:
                        encoder(char)
                    except UnicodeEncodeError as e:
                        if e.object not in unsupported_chars:
                            unsupported_chars.append(e.object)

            for char in message:
                try:
                    encoder(char)
                except UnicodeEncodeError as e:
                    if e.object not in unsupported_chars:
                        unsupported_chars.append(e.object)

filename = encode + '不支持字符.txt'
with open(filename, 'w', encoding='utf-8') as file:
    for char in unsupported_chars:
        file.write(char + '\n')

replace_rules = {}
with open('hanzi2kanji_table.txt', 'r', encoding='utf-8') as f:
    for line in f:
        key, value = line.strip().split('\t')
        replace_rules[key] = value

not_support_list = []
for key in unsupported_chars:
    if key not in replace_rules.keys():
        not_support_list.append(key)
with open('SJF映射缺少的GBK字符.txt', 'w', encoding='utf-8') as file:
    for char in not_support_list:
        file.write(char + '\n')
