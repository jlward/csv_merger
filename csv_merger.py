#! /usr/bin/env python
import optparse

usage = 'usage: ./csv_parser.py --schema="header1,header2,..." csv_file1, csv_file2, ...'
parser = optparse.OptionParser(usage=usage)
parser.add_option('--schema', dest='schema',
    help='Comma seperated header information')

def _get_needed_headers(options):
    schema = options.schema
    if schema is None:
        raise optparse.OptionValueError(usage)
    return schema.split(',')

if __name__ == '__main__':

    (opts, args) = parser.parse_args()
    headers = _get_needed_headers(opts)
    print headers, args
