import os
import csv

from pprint import pprint


class Uniter:
    def __init__(self, path):
        self.path = path

    def unite(self):
        with open(os.path.join(self.path, 'output.csv'), 'a') as resultfile:
            resultfile.write(
                'cod_loja,cod_venda,data_hora,cancelado,troca,total\n')
            for file in os.listdir(self.path):
                if not file.endswith(".CSV"):
                    print("Skipping file: " + file)
                    continue
                print("Processing file: " + file)
                with open(os.path.join(self.path, file), 'r') as csvfile:
                    data = csv.reader(csvfile, delimiter=';')
                    for row in data:
                        if row[0] == 'cod_loja':
                            continue
                        resultfile.write(str(row).replace(
                            '[', '').replace(']', '').replace("'", '')+'\n')


unite = Uniter('/home/andre/workspace/Analise_authentic_feet')
unite.unite()
