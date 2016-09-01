import base64
from Crypto.Cipher import Blowfish
import sqlite3 as sqlite
import argparse

sqlite_file_name = ''
export_file_name = ''


class Exporter:
    def __init__(self, sqlfilename, export_file=None):
        self.sqlfilename = sqlfilename
        self.export_file = export_file

    def export_to_file(self):
        print self.sqlfilename
        try:
            self.sqlconn = sqlite.connect('sqlfilename')
        except Exception:
            pass


if __name__ == '__main__':
    arg_paser = argparse.ArgumentParser()
    arg_paser.add_argument('sqlfilename')
    arg_paser.add_argument('exportfilename')
    args = arg_paser.parse_args()
    sqlite_file_name = args.sqlfilename
    export_file_name = args.export_file_name

    exporter = Exporter(sqlite_file_name, export_file_name)
    exporter.export_to_file()
