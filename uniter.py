import os
import csv

from pprint import pprint

PATH = ''
HEADER = ''
VALIDATOR = ''
COMPARATOR = 0

class Uniter:
    def __init__(self, path):
        self.path = path

    def unite(self):
        with open(os.path.join(self.path, 'output.csv'), 'a') as resultfile:
            resultfile.write(
                HEADER)
            for file in os.listdir(self.path):
                if not file.endswith(".CSV"):
                    print("Skipping file: " + file)
                    continue
                print("Processing file: " + file)
                with open(os.path.join(self.path, file), 'r') as csvfile:
                    data = csv.reader(csvfile, delimiter=';')
                    for row in data:
                        if row[COMPARATOR] == VALIDATOR:
                            continue
                        resultfile.write(str(row).replace(
                            '[', '').replace(']', '').replace("'", '')+'\n')


unite = Uniter(PATH)
unite.unite()
