
import logging
import second
import sys


logging.basicConfig(filename='app.log', filemode='a',format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

class MainMenu:
    
    def __init__(self):
        global choices
        choices={
            "1": self.register,
            "2": self.login,
            "3": self.quit
        }
        
        

    def run(self):
        
        while True:
            MainMenu.print_menu()
            while True:
                choice = input("Enter your choice: ")
                action = choices.get(choice)
                try:
                    if choice:
                        action()
                        choice=False
                    else:
                        print(f"{choice} is not a valid choice.")
                except TypeError as e:
                    logging.error(e)
                    continue
                else:
                    break
            


    def register(self):
        print("positions:\n1.student\n2.professor\n3.head of education")
        while True:
            try:
                global name,lname
                
                name,lname,position = input("Enter your name + number of your position(like this: Kilian Jornet 1): ").split(" ")
                while second.User.non_digit_validation(f'{name}{lname}') or second.User.position_validation(position):
                   name,lname,position = input("invalid!\nEnter your name + number of your position(like this: Kilian Jornet 1): ").split(" ")
                username=input("choose a username for yourself(username must include your name and last name):  ")
                while second.User.username_validation(username,name,lname) or second.User.username_repeat(username):
                   username=input("invalid\nchoose a username for yourself(username must include your name):  ")
                password=input("Please enter password should be \n1) One Capital Letter\n2) Special Character\n3) One Number \n4) Length Should be 8-18: ")
                while second.User.password_validation(password):
                    password=input("invalid \npassword should be \n1) One Capital Letter\n2) Special Character\n3) One Number \n4) Length Should be 8-18: ")
                repeatpass=input("repeat your choosen password")
                while second.User.repeat_validation(password,repeatpass):
                   repeatpass=input("incorrect\nrepeat your choosen password  ")
                
                if position=="1":
        
                    second.Student.student_registering(name,lname,username,password,repeatpass,position)
                    break
                if position=="2":
                    second.User.registering(name,lname,username,password,repeatpass,position)
                    break
                if position=="3":
                    second.User.registering(name,lname,username,password,repeatpass,position)
                    break
                
                

            except ValueError as e:
                logging.warning(e)
                continue
            
            except UnboundLocalError as e:
                logging.warning(e)
                continue
            except TypeError as e:
                logging.warning(e)
                continue
            else:
                break
                
       

    def login(self):
        global username,position_login,n
        username=input("user_name:  ")
        password=input("password:  ")
        n=second.User.object_user(username)
        position_login=n.login(username,password)

        if position_login=="1":
            student=StudentMenu()
            StudentMenu.runn(student)
           
        elif position_login=="2":
            professor=ProfessorMenu()
            ProfessorMenu.runn(professor)
            
        elif position_login=="3":
            head=HeadOfEducationMenu()
            HeadOfEducationMenu.runn(head)


    def quit(self):
        sys.exit(0)


    @staticmethod
    def print_menu():
        print("""MENU
        1. Register
        2. login
        3. Exit\n""")

class StudentMenu():
    
    def __init__(self):
        self.choices={
            "1": self.show_unit,
            "2": self.find,
            "3":self.all_unit,
            "4":self.choose,
            "5": self.quitt
        }

    def runn(self):
        
        while True:
            StudentMenu.print_menu()
            choice = input("Enter your choice: ")
            action = self.choices.get(choice)
            if choice:
                action()
            else:
                print(f"{choice} is not a valid choice.")
                logging.warning("invalid choice")

    def show_unit(self):
        n.unit_show_student()

    def find(self):
        selected_unit=input("whats the name of unit you want to search: ")
        n.search_unit_student(selected_unit)

    def all_unit(self):
        print(n.number_of_units(n.username))


    def choose(self):
        if n.number_of_units(n.username)!=0:
            selected_unit=input("whats the name of unit you want to add: ")
            n.choose_unit_student(selected_unit) 
            n.each_student(selected_unit)
            second.Course.each_course(username,selected_unit)
        else:
            print("you cant add anymore!")
            logging.info(f'{n.username} units are complitted')


    def quitt(self):
        main=MainMenu
        MainMenu.run(main)



    @staticmethod
    def print_menu():
        print("""MENU
        1. show units
        2. search unit
        3. all unit
        4. choose unit
        5. Exit\n""")



class HeadOfEducationMenu(StudentMenu):
    def __init__(self):
        self.choices={
            "1": self.show_unit,
            "2": self.find,
            "3": self.all_num_units,
            "4": self.add,
            "5": self.course_student,
            '6': self.all_student,
            "7": self.student_search,
            "8": self.student_course,
            "9": self.check_unit,
            "10": self.quitt
        }
    def runn(self):
        """Display the menu and respond to choices."""
        while True:
            HeadOfEducationMenu.print_menu()
            choice = input("Enter your choice: ")
            action = self.choices.get(choice)
            if choice:
                action()
            else:
                print(f"{choice} is not a valid choice.")
                logging.warning("invalid choice")

    def course_student(self):
        selected_unit=input("whats the name of unit you want to see the students of: ")
        n.show_student_of_course(selected_unit)

    def all_student(self):
        n.show_student_list()

    def student_search(self):
        student=input("inter the student name you are searching for:  ")
        lstudent=input("inter the student last name you are searching for:  ")
        n.search_studdent(student,lstudent)


    def student_course(self):
        student=input("inter the student username :  ")
        n.show_student_course(student)

    def check_unit(self):
        student=input("inter the student username :  ")
        n.check_student_courese(student)
 
        
    def add(self):
        while True:
            try:
                unitname,n,capacity=input("enter the name of unit with number of it and capacity in this way(unit_name,n_unit,capacity  ").split(",")
                cousrse=second.Course(unitname,n,capacity,capacity)
                cousrse.add_unit()
            except ValueError as e:
                logging.warning("invalid input")
                print(e)
                continue
            else:
                break
        

    def show_unit(self):
        n.unit_show_student()


    def all_num_units(self):
        n.number_of_units()
    

    @staticmethod
    def print_menu():
        print("""MENU
        1. show units
        2. search unit
        3. number of all units
        4. add unit
        5. students of a course
        6. all students
        7. search student
        8. courses of a student
        9. check each person units
        10. Exit\n""")

    


class ProfessorMenu(StudentMenu):
    def __init__(self):
        self.choices={
            "1": self.show_unit,
            "2": self.find,
            "3":self.choosen,
            "4":self.choose,
            "5":self.students_of_unit,
            "6": self.quitt
        }

    def runn(self):
        
        while True:
            ProfessorMenu.print_menu()
            choice = input("Enter your choice: ")
            action = self.choices.get(choice)
            if choice:
                action()
            else:
                print(f"{choice} is not a valid choice.")
                logging.warning("invalid choice")

    def show_unit(self):
        n.unit_show_professor()

    def find(self):
        selected_unit=input("whats the name of unit you want to search: ")
        n.search_unit_professor(selected_unit)

    def choosen(self):
        n.show_choosen_course(username)

    def choose(self):
        selected_unit=input("whats the name of unit you want to add: ")
        n.each_professor(selected_unit)
        n.choose_unit_professor(selected_unit) 
        
        

    def students_of_unit(self):
        selected_unit=input("whats the name of unit you want to see the students of: ")
        n.show_student_of_course(selected_unit)



    
    @staticmethod
    def print_menu():
        print("""MENU
        1. show units
        2. search unit
        3. units that choosed by you
        4. choose unit
        5. student of a course
        6. Exit\n""")