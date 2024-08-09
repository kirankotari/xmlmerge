""" XML class which contains following operations
    update xml data
    convert xml data to csv
    convert xml data to string
"""

from pandas import DataFrame
from .log import SingletonMeta
from xml.etree.ElementTree import tostring, parse

class XML(metaclass=SingletonMeta):
    data = None

    def __init__(self, path):
        self.data = parse(path).getroot()

    def update(self, path):
        data = parse(path).getroot()
        self.data.extend(data)

    def tostring(self):
        if self.data:
            return tostring(self.data).decode('utf-8')

    def to_csv(self, path):
        data, cols = [], []
        for child in self.data:
            data.append([subchild.text for subchild in child])
            cols.append(child.tag)

        df = DataFrame(data).T
        df.columns = cols
        df.to_csv(path, index=False)
