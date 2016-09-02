import crypto
import sys
sys.modules['Crypto'] = crypto

import peewee
import argparse
from db.account import Account
from db import dbProxy
from util import CryptoUtil

sqlite_file_name = ''
export_file_name = ''

teststring = 'pNPyUDezG7cRcc7dmvUTk4AEVCjXL2TVVH5q24lTN//9y65aNVsLUpG2z00L1fa3'
db = None

class Exporter:
    def __init__(self, sqlfilename, export_file=None):
        self.sqlfilename = sqlfilename
        self.export_file = export_file

    def export_to_file(self):
        dbProxy.initialize(peewee.SqliteDatabase(self.sqlfilename))
        dbProxy.connect()
        for account in Account.select().where((Account.type != 20514) & (Account.type != 20512)):
            print CryptoUtil.CryptoUtil.decrypt(account.hash, b'123456')




if __name__ == '__main__':
    arg_paser = argparse.ArgumentParser()
    arg_paser.add_argument('sqlfilename')
    arg_paser.add_argument('exportfilename')
    args = arg_paser.parse_args()
    sqlite_file_name = args.sqlfilename
    export_file_name = args.exportfilename

    exporter = Exporter(sqlite_file_name, export_file_name)
    exporter.export_to_file()
