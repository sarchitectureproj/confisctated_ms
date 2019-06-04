# importing the requests library 
import requests 
import json
import random

api_url = "http://localhost:4003"

deliverydata, categorydata, itemdata = [],[],[]

with open('./seeds/delivery.json') as json_file:  
    deliverydata = json.load(json_file)
    
with open('./seeds/category.json') as json_file:  
    categorydata = json.load(json_file)
    
with open('./seeds/item.json') as json_file:  
    itemdata = json.load(json_file)
    
for data in list(random.sample(deliverydata, k=20)):
    r = requests.post(url = api_url+"/confiscated_ms/delivery/", data = data) 
    print('Delivery Post Status:',r)

for data in list(random.sample(categorydata, k=50)):
    r = requests.post(url = api_url+"/confiscated_ms/category/", data = data) 
    print('Category Post Status:',r)
    
for data in list(random.sample(itemdata, k=500)):
    r = requests.post(url = api_url+"/confiscated_ms/items/", data = data) 
    print('Item Post Status:',r)