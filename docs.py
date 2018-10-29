'''
This will do use the Python docx module until I'm able to actually use the
Google Docs API.
'''
import os
from docx import Document

class WordDoc():
    def __init__(self):
        self.doc = Document()

    def createTestDoc(self):
        self.doc.add_heading('Good Friends')
        self.doc.add_paragraph("What's good friend?")
        self.saveOut('test1.docx')

    def openTemplate(self):
        pass
    
    def closeTemplate(self):
        pass

    def writeToTemplate(self):
        pass

    def saveOut(self, filename):
        self.doc.save(filename)

if __name__ == '__main__':
    a = WordDoc()
    a.createTestDoc()
