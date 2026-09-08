"""
Author: Tarun Balasubramaniam
Assignment Title: Dean's List
Assignment Description: Complete Student and Course classes
Due Date: 09/04/2026
Date Created: 09/03/2026
Date Last Modified: 09/03/2026
"""

class Student:
    def __init__(self, first, last, gpa):
        self.first = first
        self.last = last
        self.gpa = gpa
    def get_gpa(self):
        return self.gpa
    def get_last(self):
        return self.last
    def to_string(self):
        return self.first + ' ' + self.last + ' (GPA: ' + str(self.gpa) + ')'


class Course:
    def __init__(self):
        self.students = []
    def add_student(self, Student):
        self.students.append(Student)
    def get_deans_list(self):
        deans_list = []
        for i in range(len(self.students)):
            if self.students[i].get_gpa() >= 3.5:
                deans_list.append(self.students[i])

        return deans_list

if __name__ == "__main__":
    #data abstraction
    c = Course()
    #input
    #process
    c.add_student(Student("Henry","Nguyen",3.5))
    c.add_student(Student("Brenda","Stern",2.0))
    c.add_student(Student("Lynda","Robison",3.2))
    c.add_student(Student("Sonya","King",3.9))
    
    #output
    print("Dean's List:")
    for i in range(len(c.get_deans_list())):
        print(c.get_deans_list()[i].to_string())
    #assumptions
    """
    When passing GPA to student, GPA must be of type float or int 
    A variable of only type Student is passed
    to the add_student method
    """
    
