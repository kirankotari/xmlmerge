import sys
import pandas as pd
from xml.etree import ElementTree

from pyrsistent import get_in


def help():
    print("Usage xmlmerge  <xml-files> > <new-file>")
    print("Usage xmlmerge  -csv <csv-file> <xml-files>")
    print("                -h | --help")

def version():
    print("xmlmerge version: 1.1.1")

def get_index(given_list, element):
    try:
        return given_list.index(element)
    except ValueError:
        return None


def run():
    if len(sys.argv) <= 2:
        help()

    _help = ['-h', '--help']
    _csv = ['-csv']
    _version = ['-v', '--version']
    
    for each in _help:
        if get_index(sys.argv, each):
            help()
            return

    for each in _version:
        if get_index(sys.argv, each):
            version()
            return

    files = []
    csv_name = None
    for i in sys.argv[1:]:
        files.append(i) if '.xml' in i else None
        csv_name = i if '.csv' in i else None

    for each in _csv:
        if get_index(sys.argv, each):
            if csv_name is None:
                csv_name = "xml_to_csv.csv"
            csv(merge(files), csv_name)
            return

    if len(files) == 0:
        print("no xml files found")
        print("you can test with either ls/dir <your-input>")
        return

    print("xml files planning to merge are: ")
    print(files)
    print(merge(files))


if __name__ == '__main__':
    run()
