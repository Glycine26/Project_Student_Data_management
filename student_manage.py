#Features
#1) Add Student
#2) View Student --> All or One
#3) Update Student
#4) Delete Student
#5) Exit  


import json
from pprint import pprint

class Student:
    def __init__(self, name, age, address, marks) -> None:
        self.name = name
        self.address = address
        self.age = age
        self.marks = marks

    
class StudentManagementSystem(Student):
    def __init__(self, name:str, address:str, age:int, marks:int) -> None:
        super().__init__(name, address, age, marks)

    def data_load(self):
        with open(r'student_data.json','r')as data_file:
            profile_out = json.load(data_file)
            return profile_out
        
    def data_upload(self, profile_in):
        with open('student_data.json','w')as data_file:
            json.dump(profile_in,data_file,indent=2)

    def get_name(self):
        try:
            name = input("Enter your name: ")
            if any(char.isdigit() for char in name):
                raise ValueError("Name can't contain numbers")
            elif len(name) == 0:
                raise ValueError("Name can't be empty")
            return name
            
        except ValueError as e:
            print(e)
            # StudentManagementSystem.get_name(self)
            self.get_name()
        
    def get_age(self):
        try:
            age = input("Enter your age: ")
            if any(char.isalpha() for char in age):
                raise ValueError("Age only be integer")
            if len(age) == 0:
                raise ValueError("Age cann't be empty")
            return age
        except ValueError as e:
            print(e)
            # StudentManagementSystem.get_age(self)
            self.get_age()

    def get_address(self):
        try:
            address = input("Enter your address: ")
            if len(address) == 0:
                raise ValueError("Address cann't be empty")
            return address
        except ValueError as e:
            print(e)
            # StudentManagementSystem.get_address(self)
            self.get_address()
    
    def get_marks(self):
        try:
            marks = input("Enter your total marks: ")
            if any(char.isalpha() for char in marks):
                raise ValueError("Marks only be integer")
            if len(marks) == 0:
                raise ValueError("Marks cann't be empty")
            return marks
        except ValueError as e:
            print(e)
            # StudentManagementSystem.get_marks(self)
            self.get_marks()

    def add_student(self):
        data = self.data_load()
        student_list = {
            "Student Name" : self.get_name(),
            "Student Age" : self.get_age(),
            "Stuednt Address" : self.get_address(),
            "Student Marks" : self.get_marks()
        }

        data.append(student_list)
        self.data_upload(data)
        print("Student data successfully saved.")
        pprint(student_list, sort_dicts=False)
    
    def view_student(self):
        data = self.data_load()
        if len(data) == 0:
            print("No student data present.")
        else:
            try:
                view_type = input("All Students or One Student data(all/one): ")
                if not ((view_type == "all") or (view_type == "All") or (view_type == "one") or (view_type == "One")):
                        raise ValueError("input only be all/one")
                
                if view_type == "all" or view_type == "All":
                    print("Here is the list of all students: \n")
                    for list_student in data:
                        pprint(list_student,sort_dicts=False)
                        # break
                elif view_type == "one" or view_type == "One":
                    student_name = input("Enter the name of the student: ")
                    for one_student in data:
                        if one_student["Student Name"] == student_name:
                            pprint(one_student,sort_dicts=False)
                            # break
                    else:
                        print("No student with given name")
                        self.view_student()
            except ValueError as e:
                print(e)
                self.view_student()
    
    def delete_student(self):
        data = self.data_load()
        try:
            student_name_delete = input("Enter the name of the student to delete: ")
            student_found = False

            for student_detail in data:
                if student_detail["Student Name"] == student_name_delete:
                    data.remove(student_detail)
                    print("Data succesfully deleted.")
                    self.data_upload(data)
                    student_found = True
                    break
            
            if not student_found:
                raise ValueError(f"No student with the name {student_name_delete}")
                    
        except ValueError as e:
            print(e)
            self.delete_student()
    
    def update_student(self):
        data = self.data_load()
        
        try:
            get_name_of_student = input("Enter the name of the student to update data: ")

            matched_student_list = []
            student_found = False

            for index,matched_student_data in enumerate(data):
                # pprint(matched_student_data)
                if matched_student_data["Student Name"] == get_name_of_student:
                    matched_student_list.append(matched_student_data)
                    pprint(matched_student_list,sort_dicts=False)
                    print(f"Index : {index}")
                    student_found = True
                    break
            
            if student_found is False:
                raise ValueError(f"No student with the name {get_name_of_student}")    
                    

            if student_found is True:
                get_option = int(input("If you want to update:\nStudent Name : Press 1\nStudent Age : Press 2\nStudent Address : Press 3\nStudent Marks : Press 4\n"))
                option_list = [1,2,3,4]
                if not get_option in option_list:
                    raise ValueError("Please select 1,2,3,4")
                
                elif get_option == 1:
                    matched_student_list[0]["Student Name"] = self.get_name()

                
                elif get_option == 2:
                    matched_student_list[0]["Student Age"] = self.get_age()

            
                elif get_option == 3:
                    matched_student_list[0]["Stuednt Address"] = self.get_address()
            
                elif get_option == 4:
                    matched_student_list[0]["Student Marks"] = self.get_marks()
                
                else:
                    raise ValueError("Please select 1,2,3,4")
                

            
            data[index] = matched_student_list[0]
            print("Data Updated")
            self.data_upload(data)
            
        except ValueError as e:
            print(e)
            self.update_student()
            
    
class StudentManagement_menu(StudentManagementSystem):
    def __init__(self, name: str, address: str, age: int, marks: int) -> None:
        super().__init__(name, address, age, marks)
    
    def menu(self):
        try:
            menu_choice = int(input("Press 1 : Add Student\nPress 2 : View Student\nPress 3 : Update Student data\nPress 4 : Delete Student\nPress 5 : Exit\n"))
            menu_choice_list = [1,2,3,4,5]
            if menu_choice in menu_choice_list:
                if menu_choice == 1:
                    self.add_student()
                elif menu_choice == 2:
                    self.view_student()
                elif menu_choice == 3:
                    self.update_student()
                elif menu_choice == 4:
                    self.delete_student()
                elif menu_choice == 5:
                    print("Thank you")
            else:
                raise ValueError("You can select only 1,2,3,4,5")
        except ValueError as e:
            print(e)
            self.menu()

system_run = StudentManagement_menu(name=None,address=None,age=None,marks=None)
system_run.menu()

