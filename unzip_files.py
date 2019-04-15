# -*- coding: utf-8 -*-
import zipfile
from os import listdir
from os.path import isfile, join
from pathlib import Path
import os
import tarfile

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
DATA_DIR = os.path.join(ROOT_DIR, 'data')


def tar_file(input, output):
    tar = tarfile.open(input, "r:gz")
    file_names = tar.getnames()
    for file_name in file_names:
        tar.extract(file_name, output)
    tar.close()


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
        tar_gz_type = ".tar.gz"
        if f.rfind(zip_type) == len(f) - len(zip_type):
            target_directory = f[:-1 * len(zip_type)]
            unzip_file(str(Path(DATA_DIR) / "zip" / f), str(Path(DATA_DIR) / "unzip" / target_directory))
        elif f.rfind(tar_gz_type) == len(f) - len(tar_gz_type):
            target_directory = f[:-1 * len(tar_gz_type)]
            tar_file(str(Path(DATA_DIR) / "zip" / f), str(Path(DATA_DIR) / "unzip" / target_directory))
