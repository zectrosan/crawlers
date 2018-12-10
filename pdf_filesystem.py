import PyPDF2
import os
import sys
import hashlib
from client import Client
# creating a pdf file object


def walk_dir(client, d):
    for directory, _, files in os.walk(d):
        for i in files:
            file_path = os.path.join(directory, i)
            if not i.endswith('pdf'):
                continue

            try:
                with open(file_path, 'rb') as file:
                    # creating a pdf reader object
                    pdf = PyPDF2.PdfFileReader(file)
                    if pdf.isEncrypted:
                        print('Encountered encrypted pdf',
                              file_path, 'skipping')
                        continue
                    # printing number of pages in pdf file
                    # print(file_path, numberofpages)
                    # creating a page object and extracting text
                    document = {
                        'file': file_path,
                        'text': []
                    }
                    for i in range(pdf.numPages):
                        page = pdf.getPage(i)
                        text = page.extractText()
                        document['text'].append(text)
                    
                    doc_id = hashlib.md5(file_path.encode()).hexdigest()
                    doc_title = pdf.getDocumentInfo().title
                    client.index('file', doc_id, doc_title, document)
            except Exception as e:
                print('Error in processing', file_path)
                print(e)


if __name__ == "__main__":
    directories = [os.path.abspath('.')]

    client = Client(os.environ.get(
        'INDEX_HOST', 'http://localhost:1729'), os.environ.get('API_KEY', 'test'))

    if len(sys.argv) > 1:
        directories = sys.argv[1:]

    for directory in directories:
        print(directory)
        walk_dir(client, directory)
