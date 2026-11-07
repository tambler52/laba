class Student:
    
    def __init__(self,name,specialty):
        self.name = name
        self.specialty = specialty
        self.spisok_discp = []
        self.marks = {}

        pass
    pass




class Discipline:

    def __init__(self,name,specialty,kafedra):
        self.name = name
        self.specialty = specialty
        self.kafedra = kafedra
        pass
    pass



class Kafedra:
    def __init__(self,name):
        self.name = name
        self.spisok_discp = []
        pass
    pass


class Faculty:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.spisok_kafedr = []
        pass
    pass

faculty = Faculty("РФиКТ")


while True:
    print("МЕНЮ\n")
    print("1.зачислить студента")
    print("2.показать всех студентов")
    print('0.выход')
    choice = input("выберите действие")

    if choice == "0":
        break
    elif choice == "1":
        new_name = input("Введите имя: ")
        new_spec = input("Введите специальность: ")
        new_student = Student(new_name, new_spec)
        faculty.students.append(new_student)
        print("Студент", new_name, "зачислен")
    elif choice == "2":
        print("Список студентов:")
        for s in faculty.students:
            print("  ", s.name, "-", s.specialty)
    else:
        print("Нет такого пункта")
        
