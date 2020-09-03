import sys
from xml.etree import ElementTree


def run():
    xml_data = None
    files = sys.argv[1:]
    for filename in files:
        data = ElementTree.parse(filename).getroot()
        if xml_data is None:
            xml_data = data
        else:
            xml_data.extend(data)
    if xml_data is not None:
        print(ElementTree.tostring(xml_data).decode('utf-8'))


if __name__ == '__main__':
    run()
