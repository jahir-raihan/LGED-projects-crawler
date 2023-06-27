from bs4 import BeautifulSoup
import requests


data = requests.get(f'https://oldweb.lged.gov.bd/ProjectHome.aspx?projectID=295')

html_data = BeautifulSoup(data.text, 'html.parser')
table = html_data.find_all('table')[0]

print('https://oldweb.lged.gov.bd/' + table.tr.td.img['src'])


"""Script to get image of the project from oldweb LGED website"""
