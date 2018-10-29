import os
import configparser
from airtable import Airtable
import docs

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'


config = configparser.ConfigParser()
config.read('config.ini')

at = Airtable(config['AIRTABLE']['BASE_ID'], config['AIRTABLE']['API_KEY'])

def checkForEntries(table):
    res = at.get(table)
    print(res)

def main():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))

if __name__ == '__main__':
    # checkForEntries("tblkUqVdFMJD4o51d")
    main()