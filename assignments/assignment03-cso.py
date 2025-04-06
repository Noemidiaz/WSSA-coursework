# assignment03-cso.py
# Description:Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json"
# By Noemi Diaz



#Importing library
import requests 

# URL from the dataset in the website of CSO
URL= "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

# Getting data from CSO
response= requests.get(URL)

# If the request is successful, save the data in a cso.json file
if response.ok:
     if response.status_code == 200:
        print("Success!")
    with open("cso.json", "w", encoding="utf-8") as file:
        file.write(response.text)
else:
    print("Failed to obtain data", response.status_code)



#REFERENCES:

# Databae "Exchequer account (historical series)" from CSO: https://data.cso.ie/#
# Requests using python : https://www.geeksforgeeks.org/get-post-requests-using-python/
# Status code, the get requests and response: https://realpython.com/python-requests/