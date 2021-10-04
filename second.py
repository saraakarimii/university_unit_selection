import hashlib
import file_handler
from random import randint
import logging
import re
import datetime
import pandas as pd
 

logging.basicConfig(filename='app.log', filemode='a',format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

class User:    
    def __init__(self,name,lname,username,password,repeatpass,position):
        self.name=name
        self.lname=lname
        self.username=username
        self.password=password
        self.repeatpass=repeatpass
        self.position=position


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

    def username_validation(username,name,lname):
        if name not in username or lname not in username :
            logging.warning("invalid username it must include name and last name")
            return True

    def username_repeat(username):
        datas=file_handler.FileHandler.read_file("User")
        for i in datas:
            if i["user_name"]==username:
                logging.warning("invalid username its repetitive")
                return re.T


    def object_user(username):
        datas=file_handler.FileHandler.read_file("User")
        for i in datas:
            if i["user_name"]==username:
                if i["position"]=="1":
                    return Student(i["name"],i["l_name"],i["user_name"],i["password"],i["repeatpass"],i["position"])
                if i["position"]=="2":
                    return Professor(i["name"],i["l_name"],i["user_name"],i["password"],i["repeatpass"],i["position"])
                if i["position"]=="3":
                    return HeadOfEducation(i["name"],i["l_name"],i["user_name"],i["password"],i["repeatpass"],i["position"])

    @staticmethod
    def login(username,password):

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

    @staticmethod
    def registering(name,lname,username,password,repeatpass,position):
        file_handler.FileHandler.add_to_file({"name":name,"l_name":lname,"user_name":username,"password":password,"repeatpass":repeatpass,"position":position},"User","name","l_name","user_name","password","repeatpass","position")
        print("registered sucessfully")
        logging.info(f"new user registered with user name :{username}")
        passwordss= password.encode()
        a=hashlib.sha256(passwordss).hexdigest()
        file_handler.FileHandler.add_to_file({"user_name":username ,"password":a,"position":position},"pass","user_name","password","position")
   
        

    
class Course:
    def __init__(self,unit_name,n_unit,all_capacity,remaining_capacity):
        self.unit_name=unit_name
        self.n_unit=n_unit
        self.all_capacity=all_capacity
        self.remaining_capacity=remaining_capacity

    def add_unit(self):
        file_handler.FileHandler.add_to_file({"unit_name":self.unit_name,"n_unit":self.n_unit,"all_capacity":self.all_capacity,"remaining_capacity":self.all_capacity},"units_student","unit_name","n_unit","all_capacity","remaining_capacity")
        file_handler.FileHandler.add_to_file({"unit_name":self.unit_name,"n_unit":self.n_unit,"all_capacity":self.all_capacity,"remaining_capacity":self.all_capacity},"units_professor","unit_name","n_unit","all_capacity","remaining_capacity")
        logging.info("new unit added")

    


    def each_course(name,unit_name):
        file_handler.FileHandler.add_to_file({"name":name},f"each_course/{unit_name}students","name")

    

    

class Student(User):
    date = datetime.date.today()
    def __init__(self, name, lname, username, password, repeatpass, position,year=date.year):
        super().__init__(name, lname, username, password, repeatpass, position)
        self.year=year
        
        
    def code():
        date = datetime.date.today()
        def random_with_N_digits(n):

           range_start = 10**(n-1)
           range_end = (10**n)-1
           return randint(range_start, range_end)
       
        student_code=str(f'{date.year}{random_with_N_digits(5)}')
        datas=file_handler.FileHandler.read_file("students")
        for i in datas:
            while i["code"]==student_code:
                student_code=str(f'{date.year}{random_with_N_digits(5)}')
            else:
                print(f"its your student code:{student_code}")
                return student_code
                break

    def student_registering(name,lname,username,password,repeatpass,position):
        file_handler.FileHandler.add_to_file({"name":name,"l_name":lname,"user_name":username,"password":password,"repeatpass":repeatpass,"position":position},"User","name","l_name","user_name","password","repeatpass","position")
        print("registered sucessfully")
        logging.info(f"new user registered with user name :{username}")
        passwordss= password.encode()
        a=hashlib.sha256(passwordss).hexdigest()
        file_handler.FileHandler.add_to_file({"user_name":username ,"password":a,"position":position},"pass","user_name","password","position")
        code=Student.code()
        
        file_handler.FileHandler.add_to_file({"user_name":username ,"name":name,"l_name":lname,"year":Student.date.year,"grade":"0","code":code},"students","user_name","name","l_name","year","grade","code")
        print("you are registered as student")
        logging.info("a student registered")

    
       
    
    def number_of_units(self):
       sum=0
       datas=file_handler.FileHandler.read_file("students")
       try:
           added=file_handler.FileHandler.read_file(f"each_student/{self.username}courses")
           for i in added:
               sum+=int(i["n_unit"])
       except FileNotFoundError:
           pass
       
       for i in datas:
            if i["user_name"]==self.username:
                if int(i["grade"])>=17:
                    able_unit=25-sum
                    return able_unit
                else:
                    able_unit=18-sum
                
                    return able_unit

    def choose_unit_student(self,unit_name):
        datas=file_handler.FileHandler.change("units_student")
        data=file_handler.FileHandler.read_file("units_student")
       
        for i in range(len(data)):
            n=int((data[i])["remaining_capacity"])
            if unit_name ==(data[i])["unit_name"]:
                if (data[i])["remaining_capacity"]!=0: 
                    datas.at[i,'remaining_capacity']=n-1
                    datas.to_csv("units_student.csv", index = False, header=True)
                    logging.info(f"{unit_name} added by {self.name}")
                    break
                else:
                    print("It has no capacity")
                    logging.warning(f"{unit_name} It has no capacity any more")
        else:
            print(f"{unit_name} is not available")
            logging.warning(f"{unit_name} is not available")

    def unit_show_student(self):
        datas=file_handler.FileHandler.read_file("units_student")
        for i in datas:
            print(f'unit_name:{i["unit_name"]},Number of units:{i["n_unit"]},all_capacity:{i["all_capacity"]},remaining_capacity:{i["remaining_capacity"]}')

    def search_unit_student(self,unit_name):
        datas=file_handler.FileHandler.read_file("units_student")
        for i in datas:
            if i["unit_name"]==unit_name:
                print(f'unit_name:{i["unit_name"]},Number of units:{i["n_unit"]},all_capacity:{i["all_capacity"]},remaining_capacity:{i["remaining_capacity"]}')
        else:
            logging.warning("cant find the given unit")
            print("cant find the given unit")


    
    def each_student(self,unit_name):
        datas=file_handler.FileHandler.read_file("units_student")
        for i in datas:
            if unit_name ==i["unit_name"]:
                n_unit=i["n_unit"]
                file_handler.FileHandler.add_to_file({"unit_name":unit_name,"n_unit":n_unit},f"each_student/{self.username}courses","unit_name","n_unit")



class HeadOfEducation(Student,User):


    def number_of_units(self):
        sum=0
        datas=file_handler.FileHandler.read_file("units_student")
        for i in datas:
            sum+=int(i["n_unit"])
        print(sum)

    def show_student_list(self):
        datas=file_handler.FileHandler.read_file("students")
        for i in datas:
            print(i)

    def search_studdent(self,name,lname):
        datas=file_handler.FileHandler.read_file("students")
        for i in datas:
            if i["name"]==name and i["l_name"]==lname:
                print(i)
    

    def show_student_course(self,name):
        try:
            datas=file_handler.FileHandler.read_file(f"each_student/{name}courses")
            for i in datas:
                print(i)
        except FileNotFoundError:
            print("this student didnt choose any course")
            pass

    def check_student_courese(self,name):
        try:
           datas=file_handler.FileHandler.read_file(f"each_student/{name}courses")
           data=file_handler.FileHandler.change(f"each_student/{name}courses")
           for i in range (len(datas)):
                print(datas[i])
                check=input("if you accept this say yes")
                if check!="yes":
                    data.drop([i],axis=0,inplace=True)
                    data.to_csv(f"each_student/{name}courses.csv", index = False, header=True)
                else:
                    logging.info("unit accepted")
                    continue
        except FileNotFoundError:
            print("this student didnt choose any course")
            pass

    
class Professor(Student,User):

    def unit_show_professor(self):
        datas=file_handler.FileHandler.read_file("units_professor")
        for i in datas:
            print(f'unit_name:{i["unit_name"]},Number of units:{i["n_unit"]},all_capacity:{i["all_capacity"]},remaining_capacity:{i["remaining_capacity"]}')
     

        

    def search_unit_professor(self,unit_name):
        datas=file_handler.FileHandler.read_file("units_professor")
        for i in datas:
            if i["unit_name"]==unit_name:
                print(f'unit_name:{i["unit_name"]},Number of units:{i["n_unit"]},all_capacity:{i["all_capacity"]},remaining_capacity:{i["remaining_capacity"]}')
        else:
            logging.warning("cant find the given unit")
            print("cant find the given unit")


    def choose_unit_professor(self,unit_name):
        datas=file_handler.FileHandler.change("units_professor")
        data=file_handler.FileHandler.read_file("units_professor")
        if Professor.check_number_of_unit_professor:
            for i in range(len(data)):
                if unit_name ==(data[i])["unit_name"]:
                         datas.drop([i],axis=0,inplace=True)
                         datas.to_csv("units_professor.csv", index = False, header=True)
                         break
                else:
                    print(f"{unit_name} is not available")
                    logging.warning(f"{unit_name} is not available")
        else:
            print("you cant have more than 15 unit")
    

    def show_student_of_course(self,unit_name):
        try:
           data=file_handler.FileHandler.read_file(f"each_course/{unit_name}students")
           for i in data:
               print(i)
        except FileNotFoundError:
            print("no student choose this course")
            logging.warning("no student choose this course")
            pass

    
    def each_professor(self,unit_name):
        datas=file_handler.FileHandler.read_file("units_professor")
        for i in datas:
            if unit_name ==i["unit_name"]:
                n_unit=i["n_unit"]
                file_handler.FileHandler.add_to_file({"unit_name":unit_name,"n_unit":n_unit},f"each_professor/{self.username}professor","unit_name","n_unit")
    def check_number_of_unit_professor(self):
        units=0
        datas=file_handler.FileHandler.read_file(f"each_professor/{self.username}professor")
        for i in datas:
            units+=i['n_unit']

        if units<15:
            return True
        else:
            return False

        

    def show_choosen_course(self):
        try:
            data=file_handler.FileHandler.read_file(f"each_professor/{self.name}professor")
            for i in data:
                print(i)
        except FileNotFoundError:
            print("you didnt choose any course yet")
            logging.warning("you didnt choose any course yet")




    