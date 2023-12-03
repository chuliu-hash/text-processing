import csv
import json
import os

txt_folder = 'txt'
json_folder = 'json'

if os.path.exists(json_folder):
    os.makedirs(json_folder)

for txt_filename in os.listdir(txt_folder):
    if txt_filename.endswith('.txt'):
        txt_filepath = os.path.join(txt_folder, txt_filename)
        json_filename = os.path.splitext(txt_filename)[0] + '.json'
        json_filepath = os.path.join(json_folder, json_filename)

        with open(txt_filepath, mode='r', encoding='utf-8') as txt_file:
            txt_reader = csv.reader(txt_file)
            conversation = []

            for row in txt_reader:
                speaker = row[0].strip()
                original = row[1].strip()

                if speaker and original:
                    conversation.append({'name': speaker, 'message': original})
                elif original:
                    conversation.append({'message': original})

        with open(json_filepath, mode='w', encoding='utf-8') as json_file:
            json.dump(conversation, json_file, ensure_ascii=False, indent=4)
