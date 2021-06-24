import pandas as pd
import re
from file_manager import open_excel


# data = pd.read_excel(r'acts-user.xlsx', engine='openpyxl', header=0) 
def list_users(data: list): # pasamos el xlsx
    users = list()
    for i in data:
        if 'nan' not in str(i[1]):
            regex = re.search(r'\b([A-Za-z-\.\/\d*]{1,})\b', str(i)) # busca los nombres 
            if regex:
                users.append(regex.group())
    return set(users)
# print(open('acts-user.xlsx'))
# print(list_users(open('acts-user.xlsx')))