# File Name: api.py
# Student Name: Cam Shinker,luke elmore
# email: shinkecj@mail.uc.edu,elmorels@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/10/2025
# Course #/Section: IS 4010-002
# Semester/Year: Spring 2025
# Brief Description of the assignment: Connect to an API and complete some tasks

# Brief Description of what this module does: Contains functions/classes that complete the assignment tasks
# Citations: 

# Anything else that's relevant:

import requests
import json

class apifunctions():
    '''
    Contains functions that work with APIs
    
    '''
    def apiconnect(self, url):
        """
        Connects to the api
        @param Url string: the url that has the Api key
        """
        response = requests.get(url)
        json_string = response.content
        parsed_json = json.loads(json_string)
        return parsed_json


    def ApiData(self,parsed_json):
        """
        Gets data from the api
        @param parsed_json dict: Is the data dictionary that contains the json data
        """
       
        results = parsed_json['results']
        for planet in results[0]:
                print (planet,results[0][planet])

