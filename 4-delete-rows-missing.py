from argparse import ArgumentParser

import utils

parser = ArgumentParser()
parser.add_argument('input', help='Input csv file')
parser.add_argument('-m', '--missing-rate', type=float, default=0.5, help='Missing rate to remove rows (default: 0.5)')
parser.add_argument('output', help='Output csv file')


def main():
    args = parser.parse_args()
    headers, rows = utils.read_csv(args.input)

    for row in rows[:]:
        if sum(utils.is_null(x) for x in row) / len(row) >= args.missing_rate:
            rows.remove(row)

    utils.write_csv(args.output, headers, rows)


if __name__ == '__main__':
    main()
