import os
import json

# 声明一个空字典用于统计结果
name_counts = {}

# 设置文件夹路径
folder_path = 'json'

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)

        # 打开以UTF-8编码的JSON文件
        with open(file_path, encoding='utf-8') as file:
            data = json.load(file)

        # 统计每个人名出现的次数
        for item in data:
            if 'name' in item.keys():
                name = item['name']
                name_counts[name] = name_counts.get(name, 0) + 1


sorted_name_counts = sorted(name_counts.items(), key=lambda x: x[1], reverse=True)

# 将排序后的统计结果写入csv文件
with open('人名替换表.csv', 'w', encoding='utf-8') as file:
    file.write('原名,译名\n')
    for name, count in sorted_name_counts:
        file.write(f"{name},{count}\n")
