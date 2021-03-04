from singleton import Singleton
from invalidindex import InvalidIndexException
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