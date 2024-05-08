import csv
import json
import natsort


def bot_creation():
    csvfile = open('bots.csv', 'r')
    jsonfile = open('bots.json', 'w')

    fieldnames = ['Email', 'Password', 'Age', 'Usernames', 'DOB', 'Age Groups', 'Who is using']
    reader = csv.DictReader(csvfile, fieldnames)

    # Write the information from csv in json format
    jsonfile.write("{")
    for idx, row in enumerate(reader):
        jsonfile.write('\"bot' + str(idx) + '\": ')
        json.dump(row, jsonfile)
        jsonfile.write(',\n')
    jsonfile.write("}")


def sort_json():
    jsonfile = open('bots.json')
    jsonfile_copy = open('bots_copy.json', 'w')

    # Sort data based on bot name - botA[1-30], botT[1-30], botY[1-30]
    data = json.load(jsonfile)
    sorted_data = json.dumps({k: data[k] for k in natsort.natsorted(data)})

    # Copy sorted data in new json file
    jsonfile_copy.write(sorted_data)


if __name__ == '__main__':
    sort_json()
