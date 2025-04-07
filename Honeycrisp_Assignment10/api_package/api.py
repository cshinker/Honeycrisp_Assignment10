# File Name: api.py
# Student Name: Cam Shinker, Luke Elmore
# email: shinkecj@mail.uc.edu,elmorels@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/10/2025
# Course #/Section: IS 4010-002
# Semester/Year: Spring 2025
# Brief Description of the assignment: Connect to an API and complete some tasks

# Brief Description of what this module does: Contains functions/classes that complete the assignment tasks
# Citations: https://stackoverflow.com/questions/8816987/python-using-only-certain-keys-in-a-dictionary-for-a-for-loop

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
        @param url string: the url that has the Api key
        @return parsed_json dict: A dictionary containing data from the api
        """
        response = requests.get(url)
        json_string = response.content
        parsed_json = json.loads(json_string)
        return parsed_json

    '''
    def ApiData(self,parsed_json, planet_id):     # First function we were going to use. The function below essentially does the same thing
        """
        Gets data from the api
        @param parsed_json dict: Is the data dictionary that contains the json data
        @param planet_id int: Integer from 0-9 corresponding to a planet ID in the api
        """
       
        results = parsed_json['results']
        for attribute in results[planet_id]:
                print (attribute+":",results[planet_id][attribute])
       '''
        
    def planetLookup(self, parsed_json, planet_id):
        '''
        Takes the planet_id from the api and returns some information
        @param parsed_json dict: Is the data dictionary that contains the json data
        @param planet_id int: Integer from 0-9 corresponding to a planet ID in the api
        '''

        loop_keys = ['name','rotation_period', 'orbital_period', 'diameter', 'climate', 'terrain', 'population']
        results = parsed_json['results']
        print("Planet Information")
        for key in loop_keys:
            if key in results[planet_id]:
                print(key+":", results[planet_id][key])

