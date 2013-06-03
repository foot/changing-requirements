#!/usr/bin/env python


def query(filename, column_index, value, delimiter=","):
    pass


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description='Query a CSV file')
    parser.add_argument('filename', help='CSV file')
    parser.add_argument(
        'column_index', type=int, help='The column index to search')
    parser.add_argument('value', help='The value to search for')
    parser.add_argument(
        '--delimiter',
        default=",",
        help='The delimiter for the CSV'
    )
    args = parser.parse_args()

    rows = query(
        args.filename,
        args.column_index,
        args.value,
        delimiter=args.delimiter if args.delimiter != r"\t" else "\t",
    )

    for r in rows:
        print r
