import pandas as pd
import numpy as np
import os
import sys

source_path = sys.path[0] + '\\' + 'source'
result_path = sys.path[0]
result_dir_name = result_path + '\\' + 'result'

dirs = []


def my_read_csv(filepath, filename):
    csv_data = pd.read_csv(filepath, encoding='gbk')
    l, w, h = filepath.split('\\')[-2].split(' ')[-1].split('_')
    w = float(w.rstrip('mm'))
    h = float(h.rstrip('mm'))
    l = float(l.rstrip('mm'))
    cross = w * h
    length = l

    i = 0
    for b in a[i:i + 30]


def check_file(file_path):
    os.chdir(file_path)
    # print(os.path.abspath(os.curdir))
    all_file = os.listdir()
    files = []
    for f in all_file:
        if os.path.isdir(f):
            a = os.path.abspath(f)
            b = a.replace(source_path, "")
            dirs.append(result_dir_name + b)
            if not os.path.exists(result_dir_name + b):
                os.mkdir(result_dir_name + b)
            print(file_path + '\\' + f)
            files.extend(check_file(file_path + '\\' + f))
            os.chdir(file_path)
        else:
            if f.endswith('csv'):
                files.append(os.path.abspath(f))
                my_read_csv(files[-1], f)
    return files, dirs


file_list = check_file(source_path)
