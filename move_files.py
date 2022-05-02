import os
import shutil


source_path = ''
destination_path = ''


def move_files(src, dest):
    counter = 0
    files = os.listdir(source_path)


    for file in files:
        if os.path.getsize(f'{source_path}{file}') <= 1000:
            print(f'arquivo {file} menor que 1 Kb')
            s = src+file
            d = dest+file
            shutil.move(s, d)
            counter +=1
    print('Arquivos movidos: ', counter)


move_files(source_path, destination_path)
