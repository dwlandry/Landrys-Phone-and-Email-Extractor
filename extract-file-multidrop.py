
# coding: utf-8

# Note that this solution requires: 
# - [validate_email 1.3](https://pypi.python.org/pypi/validate_email) - `conda install -c conda-forge validate_email`

# In[140]:

import pandas as pd
import os
import sys
import re
from validate_email import validate_email
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

root = Tk()

# In[146]:

def Remove_Non_Numeric_Chars(text):
    """
    removes all non-numeric characters from the the text
    
    Arguments:
        text - the string value that you want to remove the non-numeric characters from
    Returns:
        result - string containing only numbers
    """
    #result = text.extract('(\d+)', expand=False)
    try:
        result = re.sub("\D", "", str(text))
        #if the number is 11-digits and the first digit is a 1, remove the 1
        if len(result) == 11 and result[0]=='1':
            result = result[-10:]
    except:
        result = '0' 
    return result


# In[152]:

def get_df(filePath, extension):
    if extension in (".csv"):
        df = pd.read_csv(filePath)
    elif extension in (".txt"):
        try:
            df = pd.read_table(filePath)
        except:
            #try:
            #    df = pd.read_table(filePath, encoding='cp1252')
            #except:
            #    raise
            raise
    elif extension in (".xls", ".xlsx"):
        df = pd.read_excel(filePath)
    else:
        return None
    
    return df


# In[153]:

for arg in sys.argv[1:]:
	filePath_filedrop = arg
	filePath, extension_filedrop = os.path.splitext(filePath_filedrop)
	
	filePath = filePath_filedrop
	extension = extension_filedrop
		
	df = get_df(filePath, extension)
	if df is None: exit()
	
	
	# Combine all columns into a single column.
	
	
	df_values = df.melt()['value']
	
	
	# In[145]:
	
	unique_values = df_values.unique()
	unique_values = [str(s).strip() for s in unique_values]
	
	
	# In[147]:
	
	numbers_only = [Remove_Non_Numeric_Chars(value) for value in unique_values]
	
	
	# In[148]:
	
	unique_phone_numbers = list(set([i for i in numbers_only if len(i) == 10]))
	unique_phone_numbers = ["1" + s for s in unique_phone_numbers]
	
	
	# In[149]:
	
	unique_emails = list(set([value for value in unique_values if validate_email(str(value))]))
	
	
	# In[150]:
	
	df_numbers = pd.DataFrame(unique_phone_numbers)
	df_emails = pd.DataFrame(unique_emails)
	
	
	# In[151]:
	
	df_numbers.to_csv(filePath.replace(extension, '_phone_numbers.csv'), index=False, header=False)
	df_emails.to_csv(filePath.replace(extension, '_emails.csv'), index=False, header=False)