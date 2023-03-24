from argparse import ArgumentParser

import utils

parser = ArgumentParser()
parser.add_argument('input', help='Input csv file')
parser.add_argument('-m', '--missing-rate', type=float, default=0.5, help='Missing rate to remove columns (default: 0.5)')
parser.add_argument('output', help='Output csv file')


def main():
    args = parser.parse_args()
    headers, rows = utils.read_csv(args.input)

    to_drop = []

    for col_ind in range(len(headers)):
        col = [row[col_ind] for row in rows]
        if sum(utils.is_null(x) for x in col) / len(col) >= args.missing_rate:
            to_drop.append(col_ind)

    for col_ind in reversed(to_drop):
        del headers[col_ind]
        for row in rows:
            del row[col_ind]

    utils.write_csv(args.output, headers, rows)


if __name__ == '__main__':
    main()
