#! /usr/bin/env python
import optparse
from csv import reader

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
    schema_headers = _get_needed_headers(opts)
    csv_data = {}
    first_file = True
    for arg in args:
        indexes = {}
        with open(arg) as f:
            csv_contents = list(reader(f))
        headers = csv_contents[0]
        for header in schema_headers:
            if first_file:
                email_index = headers.index('EMail')
            indexes[header] = headers.index(header)
        data = csv_contents[1:]
        for line in data:
            key = []
            for header in schema_headers:
                key.append(line[indexes[header]])
            if first_file:
                csv_data[' '.join(key)] = line
            else:
                new_key = ' '.join(key)
                if new_key not in csv_data:
                    pass
                else:
                    if line[3] != csv_data[new_key][email_index]:
                        print line
        first_file = False
        print len(csv_data)

