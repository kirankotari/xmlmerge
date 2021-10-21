import sys
import pandas as pd
from xml.etree import ElementTree


def merge(files):
    xml_data = None
    for filename in files:
        data = ElementTree.parse(filename).getroot()
        if xml_data is None:
            xml_data = data
        else:
            xml_data.extend(data)
    if xml_data is not None:
        return ElementTree.tostring(xml_data).decode('utf-8')


def csv(xml_data):
    root = ElementTree.XML(xml_data)
    data, cols = [], []
    for child in root:
        data.append([subchild.text for subchild in child])
        cols.append(child.tag)

    df = pd.DataFrame(data).T
    df.columns = cols
    print(df)


def help():
    print("Usage xmlmerge  [-csv] <xml-files> > <new-file>")
    print("                -h | --help")
    exit(-1)


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
    
    for each in _help:
        if get_index(sys.argv, each):
            help()

    files = []
    for i in sys.argv[1:]:
        files.append(i) if '.xml' in i else None

    for each in _csv:
        if get_index(sys.argv, each):
            print(csv(merge(files)))
            return

    print(merge(files))


if __name__ == '__main__':
    run()
