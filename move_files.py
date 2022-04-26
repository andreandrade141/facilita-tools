import os
import shutil


source_path = ''
destination_path = ''


def move_files(src, dest):
    files = os.listdir(source_path)

    for file in files:
        if os.path.getsize(file) <= 50:
            print(f'arquivo {file} menor que 50 B')
            s = src+file
            d = dest+file
            shutil.move(s, d)


move_files(source_path, destination_path)
