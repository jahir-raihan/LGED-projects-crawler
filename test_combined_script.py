from bs4 import BeautifulSoup
import requests
import time

data = requests.get(f'https://oldweb.lged.gov.bd/ProjectHome.aspx?projectID=268')
dic = {}

html_data = BeautifulSoup(data.text, 'html.parser')
all_tables = html_data.find_all('table')

# Data table 1 -> Broader Information Table
broader_table = all_tables[2]
bt_rows = broader_table.find_all('tr')[1:]

# Storing all data in a dictionary
for row in bt_rows:
    columns = row.find_all('td')
    dic[columns[0].get_text().strip()] = columns[2].get_text().strip()


# Data table 2 -> Short information Table
short_inf_table = all_tables[3]
st_rows = short_inf_table.find_all('tr')

# Storing all data in a dictionary
for row in st_rows:
    columns = row.find_all('td')
    dic[columns[0].get_text().strip()] = columns[1].get_text().strip()


# Data table 3 -> Getting Image url

image_table = all_tables[0]
url = 'https://oldweb.lged.gov.bd/' + image_table.tr.td.img['src']
dic['image'] = url


# So we need to track of below data points from all Tables

"""
    Table 1 -> Broader Information 
    --------
        Implementing Agency
        Project Code
        Project Name
        Date of Approval
        Cumulative Expenditure
        Physical Progress
        Progress Reporting Date
        Comment
    
    Table 2 -> Short information but valid
    -------
        Short title
        Ministry
        Executing Agency
        Approval reference
        Sector
        Status
        Funded by
        Budget
        Start Date
        Completion Date
        Name of PD
    
    Table 3 -> Image table
    ------
        Just take the image url
"""