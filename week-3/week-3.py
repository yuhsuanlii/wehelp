import time
import urllib.request, json, ssl
import csv

url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
context = ssl._create_unverified_context()
with urllib.request.urlopen(url, context=context) as jsondata:
    data = json.loads(jsondata.read().decode())
data = data['result']
funal_list=[]

for d in data.get('results'):
    postDate = time.strptime(d.get('xpostDate'), "%Y/%m/%d")
    limitDate = time.strptime("2014/12/31", "%Y/%m/%d")
    if(postDate > limitDate):
        locationPhoto = (d.get('file').lower().split('.jpg'))[0]+'.jpg'
        myString = "{},{},{},{},{}".format(d.get('stitle'),d.get('address')[5:8],d.get('longitude'),d.get('latitude'),locationPhoto) 
        mylist = myString.split(',')
        funal_list.append(mylist)

with open('output.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile,quoting=csv.QUOTE_NONE,delimiter=',',skipinitialspace=True)
    writer.writerows(funal_list)

