import csv
import math


def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = [[value.strip() for value in row]
                for row in reader]

    col_types = [str for _ in headers]
    for col_ind, col in enumerate(zip(*rows)):
        for value in col:
            try:
                int(value)
                col_types[col_ind] = int
            except ValueError:
                try:
                    float(value)
                    col_types[col_ind] = float
                except ValueError:
                    pass

    for row in rows:
        for i, value in enumerate(row):
            try:
                row[i] = col_types[i](value)
            except ValueError:
                row[i] = float('nan')

    return headers, rows


def write_csv(filename, headers, rows):
    rows = [
        [value if not is_null(value) else '' for value in row]
        for row in rows
    ]

    with open(filename, 'w+', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def is_null(value):
    return (
        value is None or
        value == '' or
        (type(value) != str and math.isnan(value))
    )
