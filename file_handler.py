import csv
from csv import DictWriter

class FileHandler:
    
    def read_file():
        with open("units.csv", 'r') as myfile:
            reader = csv.DictReader(myfile)
            return list(reader)



