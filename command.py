from student import Student
from studentregistry import StudentRegistry
from detailed_print_visitor import DetailedPrintVisitor
from brief_print_visitor import BriefPrintVisitor
from high_achiever_print_visitor import HighAchieverPrintVisitor
from low_achiever_print_visitor import LowAchieverPrintVisitor
from editcontext import EditContext
from invalidindex import InvalidIndexException

def list_students_command():
  v = DetailedPrintVisitor()
  StudentRegistry().visit_student(v)

def add_student_command():
    name = input("Введите имя студента: ")
    surname = input("Введите фамилию студента: ")
    patronymic = input("Введите отчество студента: ")
    group = input("Введите группу студента: ")
    e = Student(name,surname,patronymic,group)
    StudentRegistry().addStudent(e)
    StudentRegistry().save()

def delete_student_command():
    g = BriefPrintVisitor()
    StudentRegistry().visit_student(g)
    if g.has_students:
        index = int(input("Номер студента для удаления: "))
        if (index <= len(StudentRegistry().students)) and (index > 0):
            m = StudentRegistry().getStudent(index)
            confirm = input(f"Вы уверены что хотите удалить студента {m.name} {m.surname} {m.patronymic} ({m.group})? [y/N]").lower()
            if confirm == "y":
                StudentRegistry().deleteStudent(index)
                StudentRegistry().save()
        
def show_high_achievers_command():
    h = HighAchieverPrintVisitor()
    StudentRegistry().visit_student(h)

def show_low_achievers_command():
    l = LowAchieverPrintVisitor()
    StudentRegistry().visit_student(l)

def select_student_command():
    v = BriefPrintVisitor()
    StudentRegistry().visit_student(v)
    if v.has_students:
        index = int(input("Выберете студента для редактирования: "))
        try:
            s = StudentRegistry().getStudent(index)
            EditContext().student = s
            return True
        except InvalidIndexException:
            select_student_command()
    else:
        return False

def show_selected_student_command():
    if EditContext().student is not None:
        EditContext().student.print_detailed()

def deselect_student_command():
    if EditContext().student is not None:
        EditContext().student = None

def edit_name_command():
    a = input("Введите новое имя: ")
    EditContext().student.name = a
    StudentRegistry().save()

def edit_surname_command():
    a = input("Введите новую фамилию: ")
    EditContext().student.surname = a
    StudentRegistry().save()

def edit_patronymic_command():
    a = input("Введите новое отчество: ")
    EditContext().student.patronymic = a
    StudentRegistry().save()

def edit_group_command():
    a = input("Введите новую группу: ")
    EditContext().student.group = a 
    StudentRegistry().save()

def add_mark_command():
    a = input("Введите предмет по которому нужно добавить оценку: ")
    if  a not in EditContext().student.marks:
        b = int(input("Введите оценку: "))
        EditContext().student.marks[a] = b
        StudentRegistry().save()
    else:
        print("Оценка по этому предмету у ученика уже есть")


def edit_mark_command():
    a = input("Введите предмет который нужно изменить: ")
    if a in EditContext().student.marks:
        b = int(input("Введите новую оценку: "))
        EditContext().student.marks[a] = b
        StudentRegistry().save()
    else:
        print("Такого предмета нет у ученика")

def delete_mark_command():
    a = input("Введите предмет оценку по которому нужно удалить: ")
    if a in EditContext().student.marks:
        confirm = input(f"Вы уверены что хотите удалить оценку по предмету {a}? y/n").lower()
        if confirm == "y":
            del EditContext().student.marks[a]
            StudentRegistry().save()
    else:
        print("Такого предмета нет у ученика")