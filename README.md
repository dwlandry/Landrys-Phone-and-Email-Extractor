# landrys-phone-and-email-extractor
The purpose of this script is to extract unique phone numbers and email addresses from a csv, txt, xls, or xlsx file. 

## Usage
1. The user provides a file they wish to extract phone numbers and emails from.
2. The entire contents of the file is searched for phone numbers and email addresses - there is no need to specify particular columns to search.
3. A new csv file is automaticlly created for unique phone numbers - saved in the same directory as the source file.
4. A new csv file is automatically created for unique email addresses - saved in the same directory as the source file.

## Usage of extract-file-multidrop.py
Use this script file in conjunction with extract_multidrop.bat.  Update the .bat file so that it points to your python executable file and also the extract-file-multidrop.py file.  Once the paths to these two files are correctly referenced, you will be able to drag and drop one or more source files directly onto the .bat file.  The phone number and email file will be created for each source file included in the drop.
