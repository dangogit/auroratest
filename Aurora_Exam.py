import csv
import json
import itertools
import io

import pandas as pd
from pandas.tests.groupby.test_value_counts import df
from collections import OrderedDict
csvFilePath = r'top_linux.csv'
jsonFilePath = r'Names.json'
class Aurora_Exam():


    # Takes the file paths as arguments
    def make_json(self, csvFilePath, jsonFilePath):
        data = {}
        print("------------------------Convert a CSV to JSON--------------------------------------------------------------------")
        # Open a csv reader called DictReader
        with open(csvFilePath) as csvf:
            csvReader = csv.DictReader(csvf)

            # Convert each row into a dictionary
            # and add it to data
            for rows in csvReader:
                # Assuming a column named 'No' to
                # be the primary key
                key = rows['PID']
                data[key] = rows

        # Open a json writer, and use the json.dumps()
        # function to dump data
        with open(jsonFilePath, 'w') as jsonf:
            jsonf.write(json.dumps(data, indent=4))

    # Driver Code

    # Decide the two file paths according to your
    # computer system
    def AllUsersFun(self):
        print("------------------------Print all Users--------------------------------------------------------------------")
        self.make_json(csvFilePath, jsonFilePath)

        with open(jsonFilePath) as f1:
            jsonReader = json.load(f1)
            for data in jsonReader.values():
                print(data['USER'])

    def CommandsAndUsersFun(self):
        print("------------------------Print all commands of user--------------------------------------------------------------------")
        self.make_json(csvFilePath, jsonFilePath)
        with open(jsonFilePath) as f1:
            jsonReader = json.load(f1)

            for data in jsonReader.values():

                print(data['USER'], data['COMMAND'])


    def CommandFun(self):
        print("------------------------Get command name by pid --------------------------------------------------------------------")
        print('Enter a PID to get a Command:')
        pid = int(input())
        self.make_json(csvFilePath, jsonFilePath)

        with open(jsonFilePath) as f1:
            jsonReader = json.load(f1)

            for data in jsonReader.values():
                if int(data['PID']) == pid:
                    print(data['COMMAND'])

    def Top5CommandsFun(self):
        print("------------------------Print Top 5 Commands --------------------------------------------------------------------")
        self.make_json(csvFilePath, jsonFilePath)
        with open(jsonFilePath) as f1:
            jsonReader = json.load(f1)
            d_sorted_by_value = OrderedDict(sorted(jsonReader.items(), key=lambda x:int( x[1]['%MEM'])))

            for data in d_sorted_by_value.items()[:5]:

                print(data[1]['COMMAND'])