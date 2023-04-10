import os
import json
import csv
import pickle


def dir_traverse(directory):
    data = []
    total_size = 0


    if not os.path.exists(directory):
        return data, total_size

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            data.append({'file_name': filename, 'file_type': 'file', 'size': size})
            total_size += size

        elif os.path.isdir(file_path):
            dir_data, dir_size = dir_traverse(file_path)
            data.append({'file_name': filename, 'file_type': 'dir', 'size': dir_size, 'children': dir_data})
            total_size += dir_size
    print(f'{data}, \n')
    print(f'{total_size},\n')
    return data, total_size




def save_to_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def save_to_csv(file_path, data):
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(('file_name', 'file_type', 'size'))
        for row in data:
            writer.writerow((row['file_name'], row['file_type'], row['size']))


def save_to_pickle(file_path, data):
    with open(file_path, "wb") as f:
        pickle.dump(data, f)


def save_directory_info(directory):
    dir_data, dir_size = dir_traverse(directory)

    json_file = directory + ".json"
    csv_file = directory + ".csv"
    pickle_file = directory + ".pkl"

    save_to_json(json_file, dir_data)
    save_to_csv(csv_file, dir_data)
    save_to_pickle(pickle_file, dir_data)

    print("Directory info saved to json: {}".format(json_file))
    print("Directory info saved to csv: {}".format(csv_file))
    print("Directory info saved to pickle: {}".format(pickle_file))



save_directory_info('/Users/petrpolakov/Documents/Deep Python/venv/lesson8/')


