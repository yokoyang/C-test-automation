# coding=UTF-8
import os
import sys
from pathlib import Path

from unzip_files import DATA_DIR

if __name__ == '__main__':
    sys.path.append("C:\\Users\\Thinkpad\\Desktop\\sim_2_89")
    destination_file_dir = str(Path(DATA_DIR) / "C")
    file_list = []
    for i, j, k in os.walk(destination_file_dir):
        print(i, j, k)
        # target_file_path = str(Path(destination_file_dir) / Path(i)._cparts[-1]) + ".c"
        # target_file_path = "".join(str(target_file_path).split())
        file_list = k
        break
    print(sys.path)
    for i, f_p_1 in enumerate(file_list):
        f_1 = str(Path(destination_file_dir) / f_p_1)
        for j, f_p_2 in enumerate(file_list):
            f_2 = str(Path(destination_file_dir) / f_p_2)
            if i == j:
                continue
            else:
                # cmd_str = "sim_c.exe -p " + f_1 + " " + f_2 + " -o E:\ml\design-system\data\check.txt"
                cmd_str = "sim_c.exe -p E:\\ml\\design-system\\data\\C\\15302010033高名扬.c E:\\ml\\design-system\\data\\C\\shell.c -o E:\\ml\\design-system\\data\\check.txt"
                os.system(cmd_str)
                break
