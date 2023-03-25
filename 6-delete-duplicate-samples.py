from argparse import ArgumentParser

import utils

parser = ArgumentParser()
parser.add_argument('input', help='Input csv file')
parser.add_argument('output', help='Output csv file')


def main():
    args = parser.parse_args()
    headers, rows = utils.read_csv(args.input)

    data = []
    for row in rows[:]:
        if row not in data:
            data.append(row)

    utils.write_csv(args.output, headers, data)

if __name__ == '__main__':
    main()