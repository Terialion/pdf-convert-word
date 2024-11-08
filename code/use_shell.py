import os
import argparse
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF files to Word documents.")
    parser.add_argument("input_folder", help="The folder containing PDF files to convert.")
    parser.add_argument("output_folder", help="The folder to save the converted Word documents.")
    args = parser.parse_args()
    
    folder_pdf_convert_word(args.input_folder, args.output_folder)