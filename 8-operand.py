from argparse import ArgumentParser

import utils

parser = ArgumentParser()
parser.add_argument('input', help='Input csv file')
parser.add_argument('-c1', '--column1', help='first column name')
parser.add_argument('-c2', '--column2', help='second column name')
parser.add_argument('--operand', choices=['add', 'sub', 'div', 'mul'], default='add', help='operand - choose one: add, sub, mul, div (default: add)')
parser.add_argument('output', help='Output csv file')


def main():
    args = parser.parse_args()
    headers, rows = utils.read_csv(args.input)

    if args.column1 in headers and args.column2 in headers: 
        headers.append(args.operand)
        idx1 = headers.index(args.column1)
        idx2 = headers.index(args.column2)
    
    for row in rows:
        if args.operand == 'add':
            new_val = row[idx1] + row[idx2] 
        elif args.operand == 'sub':
            new_val = row[idx1] + row[idx2]
        elif args.operand == 'mul':
            new_val = row[idx1] * row[idx2]
        elif args.operand == 'div':
            if row[idx2] == 0:
                new_val = float('inf')
            else:    
                new_val = row[idx1] / row[idx2]
        row.append(new_val)
    
    utils.write_csv(args.output, headers, rows)

if __name__ == '__main__':
    main()