import numpy as np


def normalize(input_arr, i):
    try:
        np_input = np.array(input_arr, dtype=np.float32)
    except ValueError:
        print input_arr, i
    return np_input / np.sum(np_input)


def main_nm(csv_input_p, csv_output_p):
    out = ''
    with open(csv_input_p, 'rb') as csvfile:
        lines = csvfile.read().splitlines()
        out += lines[0] + '\n'
        for i in range(1, len(lines)):
            line_split = lines[i].split(',')
            record = normalize(line_split[2:], i)
            out += ','.join(line_split[:2]) + ',' + \
                ','.join(np.array(map(str, record)).tolist()) + '\n'
    with open(csv_output_p, 'wb') as csvfile:
        csvfile.write(out)


input_path = '/home/dat/workspace/20171/HeTGQD/NganhNhomLinhVuc.csv'
out_path = '/home/dat/workspace/20171/HeTGQD/NormaliseNhomLinhVuc.csv'

main_nm(input_path, out_path)
