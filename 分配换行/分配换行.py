import json
import os

# 定义输入和输出文件夹路径
input_folder = 'json'  # 输入JSON文件夹路径
output_folder = 'json_output'  # 输出JSON文件夹路径

# 确保输出文件夹存在，如果不存在则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的每个JSON文件
for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename)

        # 读取JSON文件
        with open(input_file_path, 'r', encoding='utf-8') as file:
            data_list = json.load(file)

        # 遍历每个字典并处理message字段
        for entry in data_list:
            message_text = entry["message"]

            # 初始化一个空字符串来存储处理后的文本
            result_text = ""

            # 每characters_per_line个字符后加一个换行符
            characters_per_line = 23
            for i in range(0, len(message_text), characters_per_line):
                result_text += message_text[i:i + characters_per_line] + '\r\n'

            # 去掉最后一个多余的换行符
            result_text = result_text.rstrip('\r\n')

            # 将处理后的文本添加到原始JSON数据中
            entry["message"] = result_text

        # 保存带有处理后文本的JSON数据到输出文件
        with open(output_file_path, 'w', encoding='utf-8') as file:
            json.dump(data_list, file, ensure_ascii=False, indent=4)
