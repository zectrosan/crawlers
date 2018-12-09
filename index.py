import PyPDF2 
import os

# creating a pdf file object 
files = [f for f in os.listdir('.') if os.path.isfile(f)]
files = filter(lambda f: f.endswith(('.pdf','.PDF')), files)
print(files)
for i in files:
    pdfFileObj = open(i, 'rb')
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # printing number of pages in pdf file 
    numberofpages=pdfReader.numPages
    print(numberofpages) 
    # creating a page object and extracting text
    for i in range(numberofpages):
        pageObj = pdfReader.getPage(i) 
        
        print(pageObj.extractText())
        # closing the pdf file object 
    pdfFileObj.close()




  
 
 
  

  
 