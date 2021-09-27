
import logging
import first
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
                name,lname,position = input("Enter your name + number of your position(like this: Kilian Jornet 1): ").split(" ")
                while first.Register.non_digit_validation(f'{name}{lname}') or first.Register.position_validation(position):
                   name,lname,position = input("invalid!\nEnter your name + number of your position(like this: Kilian Jornet 1): ").split(" ")
                username=input("choose a username for yourself(username must include your name):  ")
                while first.Register.username_validation(username,name):
                   username=input("invalid\nchoose a username for yourself(username must include your name):  ")
                password=input("Please enter password should be \n1) One Capital Letter\n2) Special Character\n3) One Number \n4) Length Should be 8-18: ")
                while first.Register.password_validation(password):
                    password=input("invalid \npassword should be \n1) One Capital Letter\n2) Special Character\n3) One Number \n4) Length Should be 8-18: ")
                repeatpass=input("repeat your choosen password")
                while first.Register.repeat_validation(password,repeatpass):
                   repeatpass=input("incorrect\nrepeat your choosen password  ")
                n=first.Register(name,lname,position,username,password,repeatpass)
                first.Register.registing(n,position)

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
        global username
        username=input("user_name:  ")
        password=input("password:  ")
        position_login=first.Login.correction(username,password)
        print(position_login)

        if position_login=="1":
            student=StudentMenu()
            StudentMenu.runn(student)
           
        elif position_login=="2":
            pass
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

class StudentMenu:
    def __init__(self):
        self.choices={
            "1": self.show_unit,
            "2": self.find,
            "3":self.all_unit,
            "4": self.quitt
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
        first.StudentAccess.unit_show()

    def find(self):
        selected_unit=input("whats the name of unit you want to search: ")
        first.StudentAccess.search_unit(selected_unit)

        


    def all_unit(self):
        first.StudentAccess.number_of_units(username)

    

    def quitt(self):
        main=MainMenu
        MainMenu.run(main)



    @staticmethod
    def print_menu():
        print("""MENU
        1. show units
        2. search unit
        3. all unit
        4. Exit\n""")

class HeadOfEducationMenu(StudentMenu):
    def __init__(self):
        self.choices={
            "1": self.show_unit,
            "2": self.find,
            "3": self.all_num_units,
            "4": self.add,
            "5": self.quitt
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


    def add(self):
        while True:
            try:
                unitname,n,capacity=input("enter the name of unit with number of it and capacity in this way(unit_name,n_unit,capacity  ").split(",")
                first.HeadOfEducationAccess.add_unit(unitname,int(n),int(capacity))
            except ValueError as e:
                logging.warning("invalid input")
                print(e)
                continue
            else:
                break
        

    def show_unit(self):
        first.HeadOfEducationAccess.unit_show()


    def all_num_units(self):
        first.HeadOfEducationAccess.number_of_units()
    

    @staticmethod
    def print_menu():
        print("""MENU
        1. show units
        2. search unit
        3. number of all units
        4. add unit
        5. Exit\n""")
