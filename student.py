class Student():
    def __init__(self,name,surname,patronymic,group):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.group = group
        self.marks ={}
    def print_detailed(self):
        print(f'''Имя: {self.name} 
Фамилия: {self.surname}
Отчество: {self.patronymic}
Группа: {self.group}
Оценки:
''',end="")
        self.printsubjects()
    def printsubjects(self):
        if len(self.marks)>0:
            for i in self.marks.keys():
                print(f'{i}-{self.marks[i]}')
        else:
            print("Оценок нет")
    def print_brief(self):
        print(f'{self.name} {self.surname} {self.patronymic} ({self.group})')

    def isHighAchiever(self):
        if len(self.marks) > 0:
            HighAchiever = True
            for i in (self.marks.values()):
                if i < 5:
                    HighAchiever = False
            return HighAchiever
        else:
            return False
    
    def isLowAchiever(self):
        LowAchiever = False
        for i in (self.marks.values()):
            if i <= 2:
                LowAchiever = True
        return LowAchiever
        