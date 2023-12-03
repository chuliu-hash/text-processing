import os
import json

origin_folder = "json_origin"
replace_folder = "json_replace"
out_folder = "json_out"


# 遍历每个文件
for filename in os.listdir(origin_folder):
    # 构建文件路径
    origin_path = os.path.join(origin_folder, filename)
    replace_path = os.path.join(replace_folder, filename)
    out_path = os.path.join(out_folder, filename)

    # 读取origin文件
    with open(origin_path, "r", encoding="utf-8") as file1:
        origin = json.load(file1)

    # 读取对应的replace文件
    with open(replace_path, "r", encoding="utf-8") as file2:
        replace = json.load(file2)

    # 确保两个JSON文件的大小相同
    if len(origin) != len(replace):
        print(f"Error: JSON files {filename} must have the same number of elements.")
        continue

    # 替换message字段的值
    for i in range(len(origin)):
        if "message" in origin[i] and "message" in replace[i]:
            origin[i]["message"] = replace[i]["message"]

        # 替换name字段的值
    for i in range(len(origin)):
        if "name" in origin[i] and "name" in replace[i]:
            origin[i]["name"] = replace[i]["name"]

    # 将修改后的JSON写入out文件夹中
    with open(out_path, "w", encoding="utf-8") as output_file:
        json.dump(origin, output_file, indent=4, ensure_ascii=False)  # 使用缩进为4的格式写入文件
