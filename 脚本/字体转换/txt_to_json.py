import json

# 读取txt文件
input_file = 'hanzi2kanji_table.txt'
output_file = 'subs_cn_jp.json'

data = {}
with open(input_file, 'r', encoding='utf-8') as file:
    for line in file:
        key, value = line.strip().split('\t')
        data[key] = value

# 将数据写入json文件
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)