import pandas as pd
import numpy as np
import os
import sys

source_path = sys.path[0] + '\\' + 'source'
result_path = sys.path[0]
result_dir_name = result_path + '\\' + 'result'

if not os.path.exists(result_dir_name):
    os.mkdir(result_dir_name)

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
    data = np.array(csv_data.values)
    mode = ""
    aa = data[0:, 1]
    max_point = np.max(aa)
    count = 0
    while (True):
        bb = aa[i:i + 200]
        i += 80
        if any(np.array(bb) == max_point):
            mode = "A"
            print(filename + "  A")
            break
        elif bb[199] < bb[0]:
            mode = "B"
            count += 1
            if count == 5:
                print(filename + "  B")
                break


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
