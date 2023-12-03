import csv
import json
import os

csv_folder = 'csv'
json_folder = 'json'

if os.path.exists(json_folder):
    os.makedirs(json_folder)

for csv_filename in os.listdir(csv_folder):
    if csv_filename.endswith('.csv'):
        csv_filepath = os.path.join(csv_folder, csv_filename)
        json_filename = os.path.splitext(csv_filename)[0] + '.json'
        json_filepath = os.path.join(json_folder, json_filename)

        with open(csv_filepath, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            conversation = []
            next(csv_reader)
            for row in csv_reader:
                speaker = row[1].strip()
                original = row[2].strip()

                if speaker and original:
                    conversation.append({'name': speaker, 'message': original})
                elif original:
                    conversation.append({'message': original})

        with open(json_filepath, mode='w', encoding='utf-8') as json_file:
            json.dump(conversation, json_file, ensure_ascii=False, indent=4)
