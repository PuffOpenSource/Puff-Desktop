import base64
import crypto
import sys
sys.modules['Crypto'] = crypto

from Crypto.Cipher import Blowfish
import peewee
from playhouse.sqlite_ext import SqliteExtDatabase
import argparse
from db.account import Account
from db import dbProxy

sqlite_file_name = ''
export_file_name = ''

db = None

class Exporter:
    def __init__(self, sqlfilename, export_file=None):
        self.sqlfilename = sqlfilename
        self.export_file = export_file

    def export_to_file(self):
        print self.sqlfilename
        dbProxy.initialize(peewee.SqliteDatabase(self.sqlfilename))
        dbProxy.connect()
        for account in Account.select():
            print account.hash




if __name__ == '__main__':
    arg_paser = argparse.ArgumentParser()
    arg_paser.add_argument('sqlfilename')
    arg_paser.add_argument('exportfilename')
    args = arg_paser.parse_args()
    sqlite_file_name = args.sqlfilename
    export_file_name = args.exportfilename

    exporter = Exporter(sqlite_file_name, export_file_name)
    exporter.export_to_file()
