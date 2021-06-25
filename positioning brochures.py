from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from time import sleep
import random
import os

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
length = 18

child_folder = {
        'folderA4': 'Brochures_A4/',
        'folderA5': 'Brochures_A5/',
        'folderA5c': 'Brochures_A5c/'
}

max_counts = [5, 16, 32]

def creating_result_file(child_folder, max_pages, format):
    pdfs = ['temporary_files/'+child_folder+filename for filename in os.listdir('temporary_files/'+child_folder)]
    merger = PdfFileMerger()

    for pdf in pdfs:
        input_PDF = PdfFileReader(pdf)
        if  input_PDF.getNumPages() > 1:
            for i in range(input_PDF.getNumPages()):
                output = PdfFileWriter()
                new_File_PDF = input_PDF.getPage(i)
                output.addPage(new_File_PDF)
                output_Name_File = pdf[:-4] +"_" + str(i + 1) + ".pdf"
                outputStream = open(output_Name_File, 'wb')
                output.write(outputStream)
                outputStream.close()
            os.remove(pdf)

    pdfs = ['temporary_files/' + child_folder + filename for filename in os.listdir('temporary_files/' + child_folder)]

    if len(pdfs) >= max_pages:
        for pdf in pdfs[:max_pages]:
            i = 0
            merger.append(pdf)
            i += 1
            if i == max_pages:
                break

        password = ''
        for i in range(length):
            password += random.choice(chars)
        merger.write("temporary_files/results/" + password + '_DONE_' + format +".pdf")
        merger.close()

        for pdf in pdfs[:max_pages]:
            i = 0
            os.remove(pdf)
            i += 1
            if i == max_pages:
                break

while True:
    print("="*25)
    pdfs_A4 = ['temporary_files/' + child_folder.get('folderA4') + filename for filename in os.listdir('temporary_files/' + child_folder.get('folderA4'))]
    pdfs_A5 = ['temporary_files/' + child_folder.get('folderA5') + filename for filename in os.listdir('temporary_files/' + child_folder.get('folderA5'))]
    pdfs_A5c = ['temporary_files/' + child_folder.get('folderA5c') + filename for filename in os.listdir('temporary_files/' + child_folder.get('folderA5c'))]
    if pdfs_A4:
        creating_result_file(child_folder.get('folderA4'), max_counts[0], 'A4')
    if pdfs_A5:
        creating_result_file(child_folder.get('folderA5'), max_counts[1], 'A5')
    if pdfs_A5c:
        creating_result_file(child_folder.get('folderA5c'), max_counts[2], 'A5c')
    print(pdfs_A4, '\n', pdfs_A5, '\n', pdfs_A5c)
    sleep(10)
