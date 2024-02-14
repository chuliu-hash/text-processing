import json
import os

def count_characters_in_json_folder(folder_path):
    total_characters = 0

    # 遍历文件夹中的所有文件
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # 检查文件是否为JSON文件
        if file_name.endswith('.json'):

            # 读取JSON文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)

            # 统计每个键对应值的字符数
            for item in json_data:
                name = item.get('name')
                message = item.get('message')
                if name:
                    total_characters += len(name)
                if message:
                    total_characters += len(message)

    return total_characters

# 指定要统计的JSON文件夹路径
json_folder_path = 'json_jp'

# 统计字符总数
total_characters = count_characters_in_json_folder(json_folder_path)
print(f'Total characters in JSON folder: {total_characters}')