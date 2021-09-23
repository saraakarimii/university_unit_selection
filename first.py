import csv
import hashlib
import datetime
from random import randint
import logging
import file_handler

logging.basicConfig(filename='app.log', filemode='a',format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

class Register:
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
            raise logging.error("repeat of password is not correct")

    def position_validation(self,position):
        if position not in range(1,4):
            raise logging.warning("position should be 1 or 2 or 3")
    
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
            logging.info("a student registered")
        if position==2:
            print("you are registered as Professor")
            logging.info("a professor registered")
        if position==3:
            print("you are registered as head of education")
            logging.info("a head of education registered")


class Login:

    def correction(self,username,password):
        datas=file_handler.FileHandler.read_file()
        a=hashlib.sha256(password.encode()).hexdigest()
        for i in datas:
            if i["username"]==username:
                if i["password"]==a:
                    print("login was successful")
                    logging.info(f"{username} logged in successfully ")
                    return True
                else:
                    print("wrong password")
                    logging.warning(f"{username} face an unsuccessful logging in")
                    return False
