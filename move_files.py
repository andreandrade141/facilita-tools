import os
import sys
import shutil


source_path = sys.argv[1]
destination_path = sys.argv[2]
size = sys.argv[3]


def move_files(src: str, dest: str, size: int) -> None:
    counter = 0
    files = os.listdir(source_path)

    for file in files:
        if os.path.getsize(f'{source_path}{file}') <= size:
            print(f'arquivo {file} menor que 1 Kb')
            s = src+file
            d = dest+file
            shutil.move(s, d)
            counter += 1
    print('Arquivos movidos: ', counter)


move_files(source_path, destination_path, size)
