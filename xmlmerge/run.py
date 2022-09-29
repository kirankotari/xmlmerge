""" Wanted to merge two or more xml files,
    and converting them to CSV file.

usage: xmlmerge 
"""

import argparse

from pathlib import Path
from logging import INFO, DEBUG

from .log import Logger

version = "1.2"


def parser() -> argparse:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs=None, help="xml files/paths/regex")
    # TODO: allow multiple file or paths or regex
    parser.add_argument("-csv", "--csv", default=None, help="the website")
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    parser.add_argument("--version", action='store_true', help="weblinks version")
    return parser.parse_args()


def validate_parser(log, args) -> bool:
    for file in args.__dict__.get('files', []):
        pass


def main():
    level=INFO

    args = parser()
    if args.__dict__.get('version', None):
        print(f"weblinks version: {version}")
        return

    if args.__dict__.get('verbosity', 0) >= 1:
        level=DEBUG

    log = Logger(level).log
    log.debug('initiate args validataion')
    if validate_parser(log, args):
        pass



def run():
    if len(sys.argv) <= 2:
        help()

    _help = ['-h', '--help']
    _csv = ['-csv']
    _version = ['-v', '--version']

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
