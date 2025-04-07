# File Name: main.py
# Student Name: Cam Shinker, Luke Elmore
# email: shinkecj@mail.uc.edu, elmorels@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/10/2025
# Course #/Section: IS 4010-002
# Semester/Year: Spring 2025
# Brief Description of the assignment: Connect to an API and complete some tasks

# Brief Description of what this module does: Contains a class which writes a dictionary to a csv file
# Citations: https://stackoverflow.com/questions/10373247/how-do-i-write-a-python-dictionary-to-a-csv-file

# Anything else that's relevant:


import csv

class csvfunction():
    '''
    Contains a function that converts a dictionary to a csv
    '''
    def __init__(self, dictionary):
        '''
        Writes a dictionary to a csv file
        @param dictionary dict: The dictionary to write
        '''
        with open("planet.csv", "w", newline="") as f:
            w = csv.DictWriter(f, dictionary.keys())
            w.writeheader()
            w.writerow(dictionary)
            