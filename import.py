import csv
import numpy as np

dest_file = 'train_2008.csv'

def load_data(file):
    with open(file,'r') as dest_f:
        data_iter = csv.reader(dest_f, delimiter = ",", quotechar = '"')
        headers = next(data_iter, None)
        data = [data for data in data_iter]

    data_array = np.asarray(data, dtype=np.float64)
    (rows, cols) = data_array.shape
    x_array = data_array[:, 0:(cols - 1)]
    y_array = data_array[:, (cols - 1)]
    return (headers, x_array, y_array)

(headers, x, y) = load_data(dest_file)
