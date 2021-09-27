import csv
import hashlib
import datetime
from random import randint
import logging
import file_handler
import re

logging.basicConfig(filename='app.log', filemode='a',format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

class Register:
    date = datetime.date.today()
    def __init__(self,name,lname,position,username,password,repeatpass,year=date.year):
        self.name=name
        self.lname=lname
        self.position=position
        self.year=year
        self.username=username
        self.password=password
        self.repeatpass=repeatpass

        passwordss= self.password.encode()
        a=hashlib.sha256(passwordss).hexdigest()
        file_handler.FileHandler.add_to_file({"user_name":username ,"password":a,"position":self.position},"pass","user_name","password","position")

    def repeat_validation(password,repeatpass):
        if password!=repeatpass:
            logging.error("repeat of password is not correct")
            return True
        

    def non_digit_validation(name):
        if any(map(str.isdigit, f'{name}')):
            logging.error("incorrect name or last name")
            return True
        else:
            return False

                

    def position_validation(position):
        if position not in ["1","2","3"]:
            logging.warning("position should be 1 or 2 or 3")
            return True
            

    def password_validation(password):
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
        match_re = re.compile(reg)
        if re.search(match_re, password):
            return False
        else:
            logging.warning("password should includ at least one uppercase letter and number")
            return True

    def username_validation(username,name):
        if name not in username:
            logging.warning("invalid username it must include name")
            return True

    
    def code(self):
        def random_with_N_digits(n):

           range_start = 10**(n-1)
           range_end = (10**n)-1
           return randint(range_start, range_end)
       
        self.student_code=str(f'{self.year}{random_with_N_digits(5)}')
        datas=file_handler.FileHandler.read_file("students")
        for i in datas:
            while i["code"]==self.student_code:
                self.student_code=str(f'{self.year}{random_with_N_digits(5)}')
            else:
                print(f"its your student code:{self.student_code}")
                break

    def registing(self,position):
        if position=="1":
            code=Register.code(self)
            file_handler.FileHandler.add_to_file({"user_name":self.username ,"name":self.name,"l_name":self.lname,"year":self.year,"grade":"0","code":code},"students","user_name","name","l_name","year","grade","code")
            print("you are registered as student")
            logging.info("a student registered")
        if position=="2":
            print("you are registered as Professor")
            logging.info("a professor registered")
        if position=="3":
            print("you are registered as head of education")
            logging.info("a head of education registered")


class Login:

    def correction(username,password):
        datas=file_handler.FileHandler.read_file("pass")
        a=hashlib.sha256(password.encode()).hexdigest()
        for i in datas:
            if i["user_name"]==username:
                if i["password"]==a:
                    print("login was successful")
                    logging.info(f"{username} logged in successfully ")
                    position=i["position"]
                    return position 
                    
                else:
                    print("wrong password")
                    logging.warning(f"{username} face an unsuccessful logging in")
                    return False
        else:
            print("we dont have user with this username")
            logging.warning("coudnt find username")
            return False
                   


class StudentAccess:
   
    def unit_show():
        datas=file_handler.FileHandler.read_file("units")
        for i in datas:
            print(f'unit_name:{i["unit_name"]},Number of units:{i["n_unit"]},all_capacity:{i["all_capacity"]},remaining_capacity:{i["remaining_capacity"]}')

    def search_unit(unit_name):
        datas=file_handler.FileHandler.read_file("units")
        for i in datas:
            if i["unit_name"]==unit_name:
                print(f'unit_name:{i["unit_name"]},Number of units:{i["n_unit"]},all_capacity:{i["all_capacity"]},remaining_capacity:{i["remaining_capacity"]}')
        else:
            logging.warning("cant find the given unit")
            print("cant find the given unit")
       

    def number_of_units(name):
        datas=file_handler.FileHandler.read_file("students")
        for i in datas:
            if i["user_name"]==name:
                if int(i["grade"])>=17:
                    able_unit=25
                    print(able_unit)
                else:
                    able_unit=18
                    print(able_unit)

class HeadOfEducationAccess(StudentAccess):
    def add_unit(unitname,number_of_unit,capacity):
        file_handler.FileHandler.add_to_file({"unit_name":unitname,"n_unit":number_of_unit,"all_capacity":capacity,"remaining_capacity":capacity},"units","unit_name","n_unit","all_capacity","remaining_capacity")
             
    def number_of_units():
        sum=0
        datas=file_handler.FileHandler.read_file("units")
        for i in datas:
            sum+=int(i["n_unit"])
        print(sum)

        
