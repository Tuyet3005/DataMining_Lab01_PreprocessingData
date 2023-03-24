from argparse import ArgumentParser

import utils

parser = ArgumentParser()
parser.add_argument('input', help='Input csv file')


def main():
    args = parser.parse_args()
    headers, rows = utils.read_csv(args.input)

    missing_names = [
        headers[i] for i, col in enumerate(zip(*rows))
        if any(utils.is_null(value) for value in col)
    ]
    print(', '.join(missing_names))


if __name__ == '__main__':
    main()
