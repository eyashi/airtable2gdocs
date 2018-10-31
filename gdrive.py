import os
from googleapiclient.discovery import build
from googleapiclient.discovery import MediaFileUpload
from httplib2 import Http
from oauth2client import file, client, tools

class Drive():
    def __init__(self):
        # Allows you to upload files to Google Docs
        self.SCOPES = 'https://www.googleapis.com/auth/drive.file'

    def connectService(self):
        # Tries to connect as 'Quickstart' when going through the auth flow
        # Fix that...
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', self.SCOPES)
            creds = tools.run_flow(flow, store)
        self.service = build('drive', 'v3', http=creds.authorize(Http()))

    def resetService(self):
        if os.path.isfile('token.json'):
            os.remove('token.json')

        self.connectService()

    def uploadFile(self, filePath):
        metadata = {
            'name': os.path.basename(filePath),
            'mimeType': 'application/vnd.google-apps.document'
            }
        media = MediaFileUpload(filePath,
                                mimetype='application/msword',
                                resumable=True)

        res = self.service.files().create(body=metadata,
                                    media_body=media,
                                    fields='id').execute()

        if res:
            return res
        else:
            return 'Failure!'

    def testConnection(self):
        # for debugging, just lists files
        results = self.service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))