import os
from pdf2docx import Converter

def folder_pdf_convert_word(inputfolder, outputfolder):
    if not os.path.exists(outputfolder):
        os.makedirs(outputfolder)

    for file in os.listdir(inputfolder):
        if file.endswith('.pdf'):
            pdf_name = file.split('.')[0]
            word_name = pdf_name + ".docx"
            cv = Converter(file)
            cv.convert(word_name)
            cv.close()
        else:
            continue

input_folder = ''
output_folder = ''
folder_pdf_convert_word(input_folder, output_folder)