import os
import configparser
from airtable import Airtable
import docs
import gdrive

config = configparser.ConfigParser()
config.read('config.ini')

# probably should roll my own Airtable class to do these special things.
at = Airtable(config['AIRTABLE']['BASE_ID'], config['AIRTABLE']['API_KEY'])

def checkForEntries(table):
    res = at.get(table)
    print(res)

def main():
    pass