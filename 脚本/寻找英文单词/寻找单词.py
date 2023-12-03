import os
import json
import re

# 输入和输出文件夹路径
input_folder = "json"
output_folder = "统计json"

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.endswith(".json"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # 读取 JSON 文件
        with open(input_path, "r", encoding="utf-8") as file:
            jsonData = json.load(file)

        word_dict = []
        flag = False
        for entry in jsonData:
            pre_zh = entry["pre_zh"]
            # 使用正则表达式匹配满足条件的英文单词
            pattern = r'[A-Za-z]{2,}'
            matches = re.findall(pattern, pre_zh)
            words = []

            if matches:
                flag = True
                # 输出匹配的单词及索引
                for word in matches:
                    words.append(word)
                word_dict.append({'索引': entry['index'], '单词': words})

        with open(output_path, mode='w', encoding='utf-8') as json_file:
            json.dump(word_dict, json_file,ensure_ascii=False, indent=4)

        if not flag:
            os.remove(output_path)



