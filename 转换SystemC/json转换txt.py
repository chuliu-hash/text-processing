import csv
import json
import os

json_folder = 'json'
txt_folder = 'txt_out'

if not os.path.exists(txt_folder):
    os.makedirs(txt_folder)

for json_filename in os.listdir(json_folder):
    if json_filename.endswith('.json'):
        json_filepath = os.path.join(json_folder, json_filename)
        txt_filename = os.path.splitext(json_filename)[0] + '.txt'
        txt_filepath = os.path.join(txt_folder, txt_filename)

        with open(json_filepath, mode='r', encoding='utf-8') as json_file:
            conversation = json.load(json_file)

        with open(txt_filepath, mode='w', encoding='utf-8', newline='') as txt_file:
            txt_writer = csv.writer(txt_file)
            txt_list = []
            for block in conversation:
                name = block.get('name', '').replace("\n", "\\n")
                message = block.get('message', '').replace("\n", "\\n")
                txt_list.append([name, message])

            txt_writer.writerows(txt_list)
