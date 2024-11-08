# pdf-to-word
Use python to convert pdf to word
## Step:
1. __Requirement:__  
    1.1 Have installed the __os__ and __pdf2docx__.
    ```python
    import os
    from pdf2docx import Converter
    ```
    1.2 Have the python ebvironment.  
2. __How to use__  
    2.1 __Use the change_in_code__  
    ```python
    input_folder = ''
    output_folder = ''
    ```  
    Fill in the folder where your pdf is located, and fill in the folder where you want to store your word.
    Run the program, then you will find the word in the output_folder.  
    2.2 __Use the shell__  
    In this way, you need to use shell to pass in the parameters. You can get help information by using this sentence:
    ```shell
    python .\pdf_word.py -h
    ```
    then you will get:
    ```shell
    usage: pdf_word.py [-h] input_folder output_folder

    Convert PDF files to Word documents.

    positional arguments:
    input_folder   The folder containing PDF files to convert.
    output_folder  The folder to save the converted Word documents.

    options:
    -h, --help     show this help message and exit
    ```
## End  
__If it helps you, you can give me a small star.__