 
# importing the requests library 
import requests 


import json

deliverydata, categorydata, itemdata = [],[],[]
api_url = "localhost:8000"

with open('delivery.json') as json_file:  
    deliverydata = json.load(json_file)
    
with open('category.json') as json_file:  
    categorydata = json.load(json_file)
    
with open('item.json') as json_file:  
    itemdata = json.load(json_file)
    
for data in deliverydata[:20]:
    r = requests.post(url = "http://"+api_url+"/confiscated_ms/delivery/", data = data) 
    print('Delivery Post Status:',r)

for data in categorydata[:20]:
    r = requests.post(url = "http://"+api_url+"/confiscated_ms/category/", data = data) 
    print('Category Post Status:',r)
    
for data in itemdata[:80]:
    r = requests.post(url = "http://"+api_url+"/confiscated_ms/items/", data = data) 
    print('Item Post Status:',r)
