import json
from re import split

# get file  json.
file_dummy = r"email slicer\data_dummy.json"

# create new file
file_data = r"email slicer\data_complete.json"

# function get data


def get_data():
    try:
        with open(file_dummy, 'r') as files:
            data = json.load(files)
    except:
        data = None
    return data

# function create file


def create_file(data):
    with open(file_data, 'w') as files:
        json.dump(data, files)


# Main
data = get_data()
data_complete = []
for i in data:
    data_silce = i['email'].split('@')
    name_temp = data_silce[0]
    domain = data_silce[1]
    username = ""
    # get username only contain alphabet
    for char in name_temp:
        if char.isalpha():
            username += char

    data_temp = {}
    data_temp['email'] = i['email']
    data_temp['username'] = username
    data_temp['domain'] = domain

    data_complete.append(data_temp)

create_file(data_complete)
