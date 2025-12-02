class Student:
    def __init__(self,name,grade):
        self.name=name
        self.__grade=grade
    def info(self):
        if self.__grade<0 or self.__grade>20:
            return False
        print(f"your name is {self.name} and your grade is {self.__grade}")
    def passig_or_falling(self):
        if self.__grade>10:
            print("ohhh you are passing")
        else:
            print("unfortunatly you are falling")
student_1=Student(input("please tell me name:"),int(input("please tell me your grade:")))
student_1.info()
student_1.passig_or_falling()
        
        
# new code
