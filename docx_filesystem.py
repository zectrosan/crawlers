import docx
import os
import sys
import hashlib
from client import Client
# creating a docx file object


def walk_dir(client, d):
    for directory, _, files in os.walk(d):
        for i in files:
            file_path = os.path.join(directory, i)
            if i.endswith('.docx'):
                try:
                    word_docx = docx.Document(file_path)
                    text = ''
                    document = {
                        'file': file_path,
                        'text': []
                    }
                    for para in word_docx.paragraphs:
                        text += para.text
                    document['text'].append(text)
                    doc_id = hashlib.md5(file_path.encode()).hexdigest()
                    # Taking doc_title as document filename
                    doc_title = i.split('.')[0]
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
