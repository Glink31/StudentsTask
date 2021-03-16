import json
import os
from singleton import Singleton
from invalidindex import InvalidIndexException
from student import Student
class StudentRegistry(metaclass=Singleton):
    def __init__(self):
        self.students = []

    def addStudent(self,student):
        self.students.append(student)

    def deleteStudent(self,index):
        self.students.remove(self.students[index-1])
        
        
    def getStudent(self,index):
        if index <= len(self.students) and index > 0:
            return self.students[index-1]
        else:
            raise InvalidIndexException("Нет такого студента")

    def getStudentCount(self):
        return len(self.students)

    def visit_student(self, visitor):
        visitor.start_visit()
        for i, student in enumerate(self.students):
            visitor.visit_student(i+1, student)
        visitor.finish_visit()

    def save(self):
        if len(self.students) > 0:
            people = []
            for i in range (len(self.students)):
                person = {}
                person["name"]=self.students[i].name
                person["surname"]=self.students[i].surname
                person["patronymic"]=self.students[i].patronymic
                person["group"]=self.students[i].group
                person["marks"]={}
                if len(self.students[i].marks)>0:
                    for j in self.students[i].marks.keys():
                        person["marks"][j]=self.students[i].marks[j]
                people.append(person)
            with open("people.json", "w") as f:
                json.dump(people,f)
    
    def load(self):
        if os.path.exists("people.json"):
            with open("people.json", "r") as f:
                people = json.load(f)
            for i in range (len(people)):
                st = Student(people[i]["name"],people[i]["surname"],people[i]["patronymic"],people[i]["group"])
                if len(people[i]["marks"]) > 0:
                    for j in (people[i]["marks"]).keys():
                        st.marks[j] = people[i]["marks"][j]
                self.addStudent(st)
            
            

            