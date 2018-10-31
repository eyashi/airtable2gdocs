# Generate Google Documents Using Airtable Forms!

Well, first generate a Word Document (.docx), then use the Google Drive API to
upload it and convert to a Google Document*

*until the Google Docs API becomes open access?

The desired end product is a form which generates a document based on submission content. Currently, the implementation will take the headers of the Airtable record and place them as headers in the document, and the contents of the record as paragraphs under those headers. It will then upload the document to Google Drive, converting it to a Google Docs document in the process. And then it will delete the Airtable record or move it to another table based on preference. Currently it just deletes it.

Next to be implemented is a templating feature, wherein you can create a document, place {header names in curly braces} and have the content of those sections filled in by the field entry cooresponding to the header.

Currently using the wonderful [Python wrapper for the Airtable API](https://github.com/nicocanali/airtable-python) (thank you!)

## To set up the Google Drive API
    1. Follow the instructions found on the [Google Drive API quickstart guide.](https://developers.google.com/drive/api/v3/quickstart/python)
    2. Save the credentials.json file retrieved in the top directory.
    3. When you run the script for the first time, you will be prompted by Google to log in and give access to "Quickstart" for file access prividges on Google Drive.
        - I need to change this so it reflects the apps name...
        - Also maybe adjust privlidges by choosing the appropriate Scope URL for Drive.
    4. The token.json generated will be your key used automatically during all future runs.

## Ideally:
This will be run as a lambda function or a cron job on a server to ping the table for updates periodically, and then generate the documents on a regular basis.