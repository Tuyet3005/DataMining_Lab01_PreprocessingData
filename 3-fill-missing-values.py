from argparse import ArgumentParser

import utils

parser = ArgumentParser()
parser.add_argument('input', help='Input csv file')
parser.add_argument('-m', '--method', choices=['mean', 'median'], default='mean',
                    help='Method to fill missing values (default: mean)')
parser.add_argument('-c', '--columns', nargs='+', help='Columns to fill')
parser.add_argument('output', help='Output csv file')


def main():
    args = parser.parse_args()
    headers, rows = utils.read_csv(args.input)

    for col_ind, col_name in enumerate(headers):
        if col_name not in args.columns:
            continue

        col = [row[col_ind] for row in rows]
        not_null = [x for x in col if not utils.is_null(x)]

        try:
            if type(col[0]) == str:
                value = max(set(not_null), key=not_null.count)
            else:
                if args.method == 'mean':
                    value = sum(not_null) / len(not_null)
                else:
                    value = sorted(not_null)[len(not_null) // 2]
        except:
            value = col[0]

        for row in rows:
            if utils.is_null(row[col_ind]):
                row[col_ind] = value

    utils.write_csv(args.output, headers, rows)


if __name__ == '__main__':
    main()
