import csv_merger

def test_getting_headers():
    class Options(object):
        def __init__(self):
            self.schema = 'header1,header2'

    options = Options()
    headers = csv_merger._get_needed_headers(options)
    assert headers, ['header1', 'header2']
