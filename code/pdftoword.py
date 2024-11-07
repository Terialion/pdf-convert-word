import pdf2doc as Convert
import os

dir_path = os.getcwd();
for file in os.listdir(dir_path):
    filetype = file.split('.')[1]
    if filetype == "pdf":
        pdf_name = file.split('.')[0]
        word_name = pdf_name + ".docx"
        cv = Convert(file)
        cv.convert(word_name)
        cv.close
    else:
        continue
