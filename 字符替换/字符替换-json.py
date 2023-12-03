import os
import json

# 读取txt文件中的替换规则
replace_rules = {}
unused_rules = {}
with open('hanzi2kanji_table.txt', 'r', encoding='utf-8') as f:
    for line in f:
        key, value = line.strip().split('\t')
        replace_rules[key] = value
        unused_rules[key] = value

# 创建存放替换后的JSON文件的文件夹
output_folder = 'json_replace'
os.makedirs(output_folder, exist_ok=True)

# 遍历json_script文件夹中的所有json文件
input_folder = 'json_script'
for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # 读取json文件
        with open(input_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # 遍历json数据，查找并替换txt中的键值对
        for item in data:
            name = item.get('name')
            message = item.get('message')
            for key, value in replace_rules.items():
                if name and key in name:
                    name = name.replace(key, value)
                    if key in unused_rules.keys():
                        del unused_rules[key]

                if message and key in message:
                    message = message.replace(key, value)
                    if key in unused_rules.keys():
                        del unused_rules[key]

            if name:
                item['name'] = name
            if message:
                item['message'] = message

        # 将更新后的json数据写回文件
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

# 将未使用的替换规则写入txt文件
unused_rules_file = 'unused_rules.txt'
with open(unused_rules_file, 'w', encoding='utf-8') as file:
    for key, value in unused_rules.items():
        file.write(f'{key}\t{value}\n')

source_characters = ''
target_characters = ''
for key, value in replace_rules.items():
    if key not in unused_rules.keys():
        source_characters += key
        target_characters += value

with open('uif_config.json', 'r', encoding='utf-8') as file2:
    data = json.load(file2)

for key, value in data.items():
    if isinstance(value, dict):
        if value.get('source_characters'):
            value['source_characters'] = source_characters
            value['target_characters'] = target_characters

with open('uif_config.json', 'w', encoding='utf-8') as file3:
    json.dump(data, file3, ensure_ascii=False, indent=4)