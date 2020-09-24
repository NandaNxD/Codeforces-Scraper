from bs4 import BeautifulSoup
import re
import requests
import csv
import os 
import pandas as pd
import json
import urllib.request,urllib.response,urllib.error


url = "https://codeforces.com/contests"

fh=open('output.txt','w')
fc=open('current.csv','w')
fp=open('previous.csv','w')
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

    sc=str(cTable)
    cidc=re.findall('<tr data-contestid=\"(.*)\">',sc)
    contestc=re.findall('<tr data-contestid.*>\n<td.*\n(.*)\r',sc)
    
    sp = str(pTable)
    cidp = re.findall('<tr data-contestid=\"(.*)\">', sp)
    contestp = re.findall('<tr data-contestid.*>\n<td.*\n(.*)\r', sp)

    res=""

    fh.write("\tCurrent or Upcoming contests\n")
    fc.write('Sl_No,Contest_ID,Contest_Name\n')
    print("\tCurrent or Upcoming contests\n")
    for i in range(len(cidc)):
        res=str(i+1)+"    "+str(str(cidc[i]))+"   "+str(contestc[i])
        fh.write(res+"\n")
        c=str(contestc[i])
        c=c.replace(",","")
        fc.write(str(i+1)+","+str(str(cidc[i]))+","+c+"\n")
        print(res)


    print("\n\n\tPrevious Contests\n")
    fh.write("\n\n\tPrevious Contests\n")
    fp.write('Sl_No,Contest_ID,Contest_Name\n')
    for i in range(len(cidp)):
        res = str(i+1)+"    "+str(str(cidp[i]))+"   "+str(contestp[i])
        fh.write(res+"\n")
        c = str(contestp[i])
        c = c.replace(",", "")
        fp.write(str(i+1)+","+str(str(cidp[i]))+","+c+"\n")
        print(res)

except Exception as ex:
    print("Network Error or No server Response or "+str(ex))

fh.close()
fp.close()
fc.close()



