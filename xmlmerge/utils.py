from glob import glob


class Utils:
    def getpath_xml(self, path):
        for xml in glob(path, recursive=True):
            yield xml