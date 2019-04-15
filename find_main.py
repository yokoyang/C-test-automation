# -*- coding: utf-8 -*-
import shutil
import zipfile
from os import listdir
from pathlib import Path
import os

from unzip_files import DATA_DIR

if __name__ == '__main__':
    unzip_file_dir = str(Path(DATA_DIR) / "unzip")
    destination_file_dir = str(Path(DATA_DIR) / "C")
    counter = 0
    filePath = unzip_file_dir
    for i, j, k in os.walk(filePath):
        print(i, j, k)
        if "main.c" in k:
            counter += 1
            target_file_path = str(Path(destination_file_dir) / Path(i)._cparts[-1]) + ".cpp"
            shutil.copyfile(str(Path(i) / "main.c"), target_file_path)
        else:
            print("a")
    print(counter)
