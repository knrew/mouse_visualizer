import csv


def read_csv(file_name):
    data = []
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            for i, c in enumerate(row):
                row[i] = float(c)
            data.append(row)
    return data


def read_csv_xy(file_name):
    x, y = [], []
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            for i, c in enumerate(row):
                row[i] = float(c)
            x.append(row[0])
            y.append(row[1])
    return x, y
