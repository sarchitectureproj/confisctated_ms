 
# importing the requests library 
import requests 


import json

data = []

with open('delivery.json') as json_file:  
    data = json.load(json_file)
    

    
for d in data:
    r = requests.post(url = "http://localhost:8000/confiscated_ms/delivery/", data = data[2]) 
    print(r)

