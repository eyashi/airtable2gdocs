import os
import configparser
from airtable import Airtable
import gdocs
import docx

config = configparser.ConfigParser()
config.read('config.ini')

at = Airtable(config['AIRTABLE']['BASE_ID'], config['AIRTABLE']['API_KEY'])

def checkForEntries(table):
    res = at.get(table)
    print(res)

if __name__ == '__main__':
    checkForEntries("tblkUqVdFMJD4o51d")