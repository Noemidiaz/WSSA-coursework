# assignment03-cso.py
#Description:Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json"
# By Noemi Diaz

import requests

URL= "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

response= requests.get(URL)
print (response.json())