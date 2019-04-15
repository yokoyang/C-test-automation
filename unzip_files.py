# -*- coding: utf-8 -*-
import zipfile
from os import listdir
from os.path import isfile, join
from pathlib import Path
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
DATA_DIR = os.path.join(ROOT_DIR, 'data')


def unzip_file(input, output):
    """Unzip file.
    Args:
        input (str): Zip file.
        output (str): Target directory.
    """
    with zipfile.ZipFile(input, 'r') as zip:
        zip.extractall(output)


if __name__ == '__main__':
    zip_file_dir = str(Path(DATA_DIR) / "zip")
    onlyfiles = [f for f in listdir(zip_file_dir) if isfile(join(zip_file_dir, f))]
    print(onlyfiles)
    for f in onlyfiles:
        zip_type = ".zip"
        if f.rfind(zip_type) == len(f) - len(zip_type):
            target_directory = f[:-1 * len(zip_type)]
            unzip_file(str(Path(DATA_DIR) / "zip" / f), str(Path(DATA_DIR) / "unzip" / target_directory))
