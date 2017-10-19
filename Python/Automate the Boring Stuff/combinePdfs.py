#!python 3
# combinePdfs.py - Combines all the PDFs in the current working directory into
# a single PDF

import PyPDF2, os
#Get all the PDF filenames
pdfFiles=[]
for filename in os.listdir('.'):  # returns a list of all files in the cwd
	if filename.endswith('.pdf'): # finds the files with the .pdf extension
		pdfFiles.append(filename) # adds these files to pdfFiles list
pdfFiles.sort(key=str.lower) # The list gets sorted in alphabetical order
pdfWriter = PyPDF2.PdfFileWriter() # pdfWriter object created to hold the combined PDF pages

# Look through all the PDF files
for filename in pdfFiles:
	pdfFileObj = open(filename, 'rb') # each file from the list opens in read-binary mode and an object is created for each
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj) # Each object is passed to PyPDF2.PdfFileReader() to create a PdfFileReader object for the PDF file

	# Loop through all the pages (except the first) and add them
	for pageNum in range(1, pdfReader.numPages): # PyPDF2 considers 0 to be the first page
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()