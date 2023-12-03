import csv
import json
import os

# 输入和输出文件夹的路径
json_folder = 'json'
csv_folder = 'csv'


# 遍历json文件夹中的JSON文件
for json_filename in os.listdir(json_folder):
    if json_filename.endswith('.json'):
        json_filepath = os.path.join(json_folder, json_filename)
        csv_filename = os.path.splitext(json_filename)[0] + '.csv'
        csv_filepath = os.path.join(csv_folder, csv_filename)

        # 读取JSON文件
        with open(json_filepath, mode='r', encoding='utf-8') as json_file:
            message_list = json.load(json_file)

        # 打开CSV文件以读取
        with open(csv_filepath, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            updated_rows = [next(csv_reader)]  # 存储更新后的行数据

            for row in csv_reader:
                if row[2].strip():
                    message = message_list.pop(0)['message']
                    row[3] = message

                updated_rows.append(row)

        # 将更新后的数据写回CSV文件
        with open(csv_filepath, mode='w', encoding='utf-8', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(updated_rows)
