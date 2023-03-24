from argparse import ArgumentParser

import utils

parser = ArgumentParser()
parser.add_argument("input", help="Input csv file")


def main():
    args = parser.parse_args()
    headers, rows = utils.read_csv(args.input)

    lines_with_missing_data = len(
        [row for row in rows if any([utils.is_null(x) for x in row])]
    )
    print(lines_with_missing_data)


if __name__ == "__main__":
    main()
