import csv
import hashlib
import datetime
from random import randint
import logging
import file_handler

logging.basicConfig(filename='app.log', filemode='a',format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

class Register:
    user_Capacity=1250000
    def __init__(self,position,username,password,repeatpass):
        self.position=self.position_validation(position)
        self.username=username
        self.password=password
        self.repeatpass=self.repeat_validation(repeatpass)
        passwordss= self.password.encode()
        a=hashlib.sha256(passwordss).hexdigest()
        with open("passwords.cvs","a") as users_pass:
            fieldnames = ['username', 'password']    
            writer = csv.DictWriter(users_pass, fieldnames=fieldnames) 
            writer.writeheader()    
            writer.writerow({'username':f'{username}', 'password': f'{a}'})

    def repeat_validation(self,repeatpass):
        if self.password!=repeatpass:
            raise Exception

    def position_validation(self,position):
        if position not in range(1,4):
            raise Exception
    
    def code(self):
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        def random_with_N_digits(n):
           range_start = 10**(n-1)
           range_end = (10**n)-1
           return randint(range_start, range_end)

        self.student_code=str(f'{year}{random_with_N_digits(5)}')
        print(self.student_code)

    def registing(self,position):
        if position==1:
            Register.code()
            print("you are registered as student")
        if position==2:
            print("you are registered as Professor")
        if position==3:
            print("you are registered as head of education")
