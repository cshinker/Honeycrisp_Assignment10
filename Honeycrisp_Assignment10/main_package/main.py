# File Name: main.py
# Student Name: Cam Shinker,luke elmore
# email: shinkecj@mail.uc.edu, elmorels@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/10/2025
# Course #/Section: IS 4010-002
# Semester/Year: Spring 2025
# Brief Description of the assignment: Connect to an API and complete some tasks

# Brief Description of what this module does: Contains the entry point code for the assignment
# Citations: 

# Anything else that's relevant:

import json 
from api_package.api import *
if __name__ == "__main__":
    
    api = apifunctions()

    parsed_json = api.apiconnect("https://swapi.dev/api/planets/")

    #api.ApiData(parsed_json, 1)   # The was our original function, leaving it as a comment just for commit documentation
    api.planetLookup(parsed_json, 1)
  
