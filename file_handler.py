import csv
from csv import DictWriter
import pandas as pd

class FileHandler:
    
    def read_file(name):
        with open(f"{name}.csv", 'r') as myfile:
            reader = csv.DictReader(myfile)
            return list(reader)

    def add_to_file(new_value,name,*argv):
        field_name=[]
        for arg in argv:
            field_name.append(arg)    
        with open(f"{name}.csv", 'a') as myfile:
            writer = DictWriter(myfile,fieldnames=field_name)
            if myfile.tell() == 0:
                writer.writeheader()
            writer.writerows([new_value])

    def change(filename):
        df= pd.read_csv(f"{filename}.csv")
        return df

        

