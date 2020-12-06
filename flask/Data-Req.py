"""
Created on Tue Aug 25 05:18:03 2020

@author: DELL
"""

# importing the requests library 
import requests 
from input_data import data_in
 
# api-endpoint 
URL = 'http://127.0.0.1:5000/predict'
  
# Headers given here 
headers = {"Content-Type":"application/json"}
  
# Data given here 
data = {"input":data_in}
  
# sending get request and saving the response as response object 
r = requests.get(URL, headers = headers,json=data) 
  
# extracting data in json format 
r.json() 