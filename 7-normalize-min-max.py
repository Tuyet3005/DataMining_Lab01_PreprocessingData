from argparse import ArgumentParser

import utils
import math 

parser = ArgumentParser()
parser.add_argument('input', help='Input csv file')
parser.add_argument('output', help='Output csv file')
parser.add_argument('-m', '--scaler', choices=['min-max', 'Z-score'], default='min-max',
                    help='Scaler for normalization')
def main():
    args = parser.parse_args()
    headers, rows = utils.read_csv(args.input)
    
    for col_idx, header in enumerate(headers):
        values = [row[col_idx] for row in rows]
        
        if type(values[0]) == str or col_idx == 0:
            pass
        else:
            if args.scaler == 'min-max':
                min_val, max_val = min(values), max(values)
                print(min_val, max_val)
                if (min_val == max_val):
                    for row in rows:
                        row[col_idx] = 0 if min_val == 0 else 1
                else:            
                    for row in rows:
                        row[col_idx] = (float(row[col_idx]) - min_val) / (max_val - min_val)
            else:
                not_null = [x for x in values if not utils.is_null(x)]
                mean = sum(not_null) / len(not_null)
                xx = [(x-mean)*(x-mean) for x in not_null]
                STD = math.sqrt(sum(xx)/(len(not_null) - 1))  

                for row in rows:
                    row[col_idx] = (float(row[col_idx]) - mean) / STD if STD != 0 else 0
                
    utils.write_csv(args.output, headers, rows)

if __name__ == '__main__':
    main()