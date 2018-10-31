import os
import configparser
from airtable import Airtable
from docs import WordDoc
from gdrive import Drive

config = configparser.ConfigParser()
config.read('config.ini')

# probably should roll my own Airtable class to do these special things.
at = Airtable(config['AIRTABLE']['BASE_ID'], config['AIRTABLE']['API_KEY'])
drive = Drive()
doc = WordDoc()

drive.connectService()

def checkForEntries():
    return at.get(config['AIRTABLE']['TABLE_ID'])

def main():
    # probably should be done async bc of the API calls... but will
    # just bodge this together for now.

    resp = checkForEntries()
    if len(resp['records']) > 0:
        for record in resp['records']:
            docPath = doc.writeDoc(record)
            upload_resp = drive.uploadFile(docPath)
            print(upload_resp)

if __name__ == '__main__':
    main()