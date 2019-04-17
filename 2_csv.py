from pathlib import Path

import pandas as pd

from unzip_files import DATA_DIR

if __name__ == '__main__':
    check_file_path = str(Path(DATA_DIR) / "check.txt")
    df = pd.DataFrame()

    for line in open(check_file_path):
        st_list = line.split(".c")
        start_name = ""
        end_name = ""
        for i, st in enumerate(st_list):
            if i == 2:
                continue
            st_num = st[st.rfind("\\") + 1:]
            if i == 0:
                start_name = st_num
            elif i == 1:
                end_name = st_num
        n_list = line.split(" %")
        sim = ""
        for n in n_list:
            sim = n[n.rfind("for") + 4:] + "%"
            break
        df.loc[start_name, end_name] = sim
        df.loc[start_name, start_name] = "0%"
    df.to_csv("test.csv")
