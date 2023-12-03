import json
import os


input_folder = "json"
output_folder = "json_output"

# 创建输出文件夹如果不存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename)

        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            data = json.load(input_file)

            for obj in data:
                if "pre_jp" in obj.keys() and "pre_zh" in obj.keys():
                    pre_jp = obj["pre_jp"]
                    pre_zh = obj["pre_zh"]

                    if pre_jp.startswith("\\b") and not pre_zh.startswith("\\b"):
                        pre_zh = "\\b" + pre_zh
                        obj["pre_zh"] = pre_zh

            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                json.dump(data, output_file, indent=4, ensure_ascii=False)


