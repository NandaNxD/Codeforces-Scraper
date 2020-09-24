from bs4 import BeautifulSoup
import re,requests 
import json
import urllib.request,urllib.response,urllib.error

url = "https://codeforces.com/contests"

try:
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'lxml')
    
    cTable = soup.find("div", {"class":"datatable"})
    pTable = soup.find("div", {"class": "contests-table"})
    
    if(pTable is None):
        print('Previous Table Empty')
        exit(0)
    if(cTable is None):
        print('Current Table Empty')
        exit(0)

    s=str(cTable)
    crow=re.findall('<tr data-contestid=\"(.*)\">',str(cTable))
    ccontest=re.findall('<tr data-contestid.*>\n<td.*\n(.*)\r',s)
    print(crow)
    print(ccontest)
    

except Exception as ex:
    print("Network Error or No server Response or "+str(ex))

