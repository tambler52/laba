class Student:
    
    def __init__(self,name,specialty,student_id):
        self.id = student_id
        self.name = name
        self.specialty = specialty
        self.spisok_discp = []
        self.marks = {}

        




class Discipline:

    def __init__(self,name,specialty,kafedra):
        self.name = name
        self.specialty = specialty
        self.kafedra = kafedra
        



class Kafedra:
    def __init__(self,name):
        self.name = name
        self.spisok_discp = []
        


class Faculty:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.spisok_kafedr = []
    def find_student(self, stud_id):
        student_found = None
        for student in self.students:
            if student.id == stud_id:
                student_found = student
                break
        if student_found is None:
            print("нет такого студента")
            return None
        return student_found
        

    def zachislit_studenta(self, name, specialty,stud_id):
        new_student = Student(name, specialty,stud_id)
        self.students.append(new_student)
        print("студент", name, "зачислен")

    def otchislit_studenta(self, stud_id):
        student = self.find_student(stud_id)
        if student is None:
            print("студент не найден")
            return None
        self.students.remove(student)
        print("студент", student.name, "отчислен")

    def zapisat_na_discp(self, stud_id, discp_name):
        student = self.find_student(stud_id)
        if student is None:
            print("студент не найден")
            return None
        
        discp = None
        for kaf in self.spisok_kafedr:
            for discpline in kaf.spisok_discp:
                if discpline.name == discp_name:
                    discp = discpline
                    break
            if discp is not None:
                break
        
        if discp is None:
            print("дисциплина не найдена")
            return None
        
        if student.specialty not in discp.specialty:
            print("ошибка: дисциплина не для этой специальности")
            return None
        
        if discp in student.spisok_discp:
            print("студент уже записан на эту дисциплину")
            return None
        
        student.spisok_discp.append(discp)
        print("студент", student.name, "записан на", discp_name)

    def vstavit_ocenku(self, stud_id, discp_name, mark):
        student = self.find_student(stud_id)
        if student is None:
            print("студент не найден")
            return None
        
        discp = None
        for discpline in student.spisok_discp:
            if discpline.name == discp_name:
                discp = discpline
                break
        
        if discp is None:
            print("студент не записан на эту дисциплину")
            return
        
        if mark < 2 or mark > 10:
            print("оценка должна быть от 2 до 10")
            return None
        
        student.marks[discp.name] = mark
        print("оценка", mark, "выставлена студенту", student.name, "по", discp_name)

    def udalit_s_discp(self, stud_id, discp_name):
        student = self.find_student(stud_id)
        if student is None:
            print("студент не найден")
            return None
        
        discp = None
        for discpline in student.spisok_discp:
            if discpline.name == discp_name:
                discp = discpline
                break
        
        if discp is None:
            print("студент не записан на эту дисциплину")
            return None
        
        student.spisok_discp.remove(discp)
        student.marks.pop(discp.name, None)
        print("студент", student.name, "удалён c дисциплины", discp_name)

    def perevesti_semestr(self, stud_id):
        student = self.find_student(stud_id)
        if student is None:
            print("студент не найден")
            return None
        
        if len(student.spisok_discp) == 0:
            print("нет дисциплин для перевода")
            return None
        
        vse_ocenki_est = True
        for discpline in student.spisok_discp:
            if discpline.name not in student.marks:
                vse_ocenki_est = False
                break
        
        if not vse_ocenki_est:
            print("не все дисциплины изучены")
            return None
        
        vse_horosho = True
        for grade in student.marks.values():
            if grade < 4:
                vse_horosho = False
                break
        
        if not vse_horosho:
            print("есть неудовлетворительные оценки")
            return None
        
        student.spisok_discp = []
        student.marks = {}
        print("студент", student.name, "переведён в следующий семестр")

    def vedomost(self, stud_id):
        student = self.find_student(stud_id)
        if student is None:
            print("студент не найден")
            return None
        
        with open("vedomost.txt", "w", encoding="utf-8") as file:
            file.write("id студента: " + str(student.id))
            file.write("студент: " + student.name + "\n")
            file.write("специальность: " + student.specialty + "\n")
            file.write("дисциплины и оценки:\n")
            
            for discp in student.spisok_discp:
                ocenka = student.marks.get(discp.name, "нет оценки")
                file.write("  " + discp.name + " (кафедра: " + discp.kafedra.name + "): " + str(ocenka) + "\n")
            
            if len(student.marks) > 0:
                summa = 0
                for grade in student.marks.values():
                    summa = summa + grade
                sredniy = summa / len(student.marks)
                file.write("средний балл: " + str(sredniy) + "\n")
            else:
                file.write("средний балл: нет оценок\n")
        
        print("ведомость сохранена в файл vedomost.txt")
       

faculty = Faculty("РФиКТ")
kafedra = Kafedra("Биоинформатика")

d1 = Discipline("Биоинформатика", ["прикладная информатика", "кибербезопасность"], kafedra)
d2 = Discipline("Базы данных", ["прикладная информатика"], kafedra)


kafedra.spisok_discp.append(d1)
kafedra.spisok_discp.append(d2)
faculty.spisok_kafedr.append(kafedra)



while True:
    print("МЕНЮ\n")
    print("1.зачислить студента")
    print("2.показать всех студентов")
    print('3.отчислить студента')
    print("4.запись на дисциплину")
    print("5.ыставить оценку")
    print("6.удалить студента c дисциплины")
    print("7.перевести студента в следующий семестр")
    print("8.записать в файл")
    print('0.выход')

    choice = input("выберите действие")

    if choice == "0":
        break
    elif choice == "1":
        new_name = input("введите имя:")
        new_spec = input("введите специальность:")
        stud_id = int(input("введите id:"))
        new_student = Student(new_name, new_spec, stud_id)
        faculty.zachislit_studenta(new_name,new_spec,stud_id)
        print("студент", new_name, "зачислен")
    elif choice == "2":
        print("список студентов:")
        for student in faculty.students:
            print("  ", student.name, 'id',student.id, "-", student.specialty)
    elif choice == '3':
        stud_id = int(input("введите id студента для отчисления:"))
        faculty.otchislit_studenta(stud_id) 
    elif choice == "4":
       stud_id = int(input("введите id студента:"))
       discp_name = input("введите название дисциплины")
       faculty.zapisat_na_discp(stud_id,discp_name)
       
    elif choice == '5':
       stud_id = int(input("введите id студента:"))
       discp_name = input("введите название дисциплины")
       mark = int(input("введите отметку"))
       faculty.vstavit_ocenku(stud_id,discp_name,mark)
       
    elif choice == '6':
        stud_id = int(input("введите id студента:"))
        discp_name = input("введите дисциплину")
        faculty.udalit_s_discp(stud_id,discp_name)
    

    elif choice == '7':
        stud_id = int(input("введите id студента:"))
        faculty.perevesti_semestr(stud_id)
        
    elif choice == '8':
        stud_id = int(input("введите id студента:"))
        faculty.vedomost(stud_id) 
    else:
        print("нет такого пункта")
        
