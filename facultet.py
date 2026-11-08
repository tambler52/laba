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
kafedra = Kafedra("Биоинформатика")

d1 = Discipline("Биоинформатика", "прикладная информатика", kafedra)
d2 = Discipline("Базы данных", "прикладная информатика", kafedra)


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
        new_name = input("введите имя: ")
        new_spec = input("введите специальность: ")
        new_student = Student(new_name, new_spec)
        faculty.students.append(new_student)
        print("студент", new_name, "зачислен")
    elif choice == "2":
        print("список студентов:")
        for s in faculty.students:
            print("  ", s.name, "-", s.specialty)
    elif choice == '3':
        name_to_delete = input("введите имя студента для отчисления")
        for student in faculty.students:
            if student.name == name_to_delete:
                faculty.students.remove(student)
                print("студент",name_to_delete,"отчислен")
                break
        else:
            print("студент не найден")   
    elif choice == "4":
       stud_name = input()
       discp_name = input()

       naydennyy_student = None
       for student in faculty.students:
           if student.name == stud_name:
               naydennyy_student = student
               break
       if naydennyy_student is None:
           print("студент не найден")
           continue
    
       naydennaya_discp = None
       for kafedra in faculty.spisok_kafedr:
           for discp in kafedra.spisok_discp:
               if discp.name == discp_name:
                  naydennaya_discp = discp
                  break
       if naydennaya_discp is None:
           print("нет такой дисциплины")
           continue
       if naydennaya_discp.specialty != naydennyy_student.specialty:
           print("Ошибка: не для этой специальности")
           continue
       if naydennaya_discp in naydennyy_student.spisok_discp:
           print("Уже записан")
           continue
       naydennyy_student.spisok_discp.append(naydennaya_discp)
       print("Студент записан")
        
       
    elif choice == '5':
       print("введите имя студента")
       stud_name = input()
       print("введите дисциплину")
       discp_name = input()
       mark = int(input())
       naydennyy_student = None
       for student in faculty.students:
           if student.name == stud_name:
               naydennyy_student = student
               break
       if naydennyy_student is None:
        print("такого студента нет")
        continue
       naydennaya_discp = None
       for discp in naydennyy_student.spisok_discp:
           if discp.name == discp_name:
               naydennaya_discp = discp
               break
       if naydennaya_discp is None:
           print("такой дисциплины нету")
           continue
        
       if mark < 2 or mark > 10:
           print("оценка должна быть от 2 до 10")
           continue    
       
       naydennyy_student.marks[naydennaya_discp.name] = mark
       print("оценка", mark, "выставлена студенту", stud_name, "по", discp_name)

    elif choice == '6':
        stud_name = input()
        discp_name = input()
        naydennyy_student = None
        for student in faculty.students:
            if student.name == stud_name:
                naydennyy_student = student
                break
        if naydennyy_student is None:
            print("такого студента нет")
            continue   
        naydennaya_discp = None
        for discp in naydennyy_student.spisok_discp:
           if discp.name == discp_name:
               naydennaya_discp = discp
               naydennyy_student.spisok_discp.remove(discp)
               naydennyy_student.marks.pop(discp.name, None)
               print("студент удален c дисциплины")
               break
        if naydennaya_discp is None:
           print("такой дисциплины нету")
           continue  


    elif choice == '7':
        stud_name = input()
        naydennyy_student = None
        for student in faculty.students:
            if student.name == stud_name:
                naydennyy_student = student
                break
        if naydennyy_student is None:
            print("такого студента нет")
            continue

        if len(naydennyy_student.spisok_discp) == 0: 
            print("нет дисциплин")
            continue
        vse_ocenki_est = True
        for discp in naydennyy_student.spisok_discp:
            if discp.name not in naydennyy_student.marks:
                vse_ocenki_est = False
                break
        if not vse_ocenki_est:
            print("не все дисциплины изучены")
            continue
        vse_horosho = True
        for grade in naydennyy_student.marks.values():
            if grade < 4:
                vse_horosho = False
                break
        if not vse_horosho: 
            print("Есть неудовлетворительные оценки")
            continue 
        naydennyy_student.spisok_discp = []
        naydennyy_student.marks = {}
        print("Студент переведён в следующий семестр")
                
    elif choice == '8':
        stud_name = input()
        naydennyy_student = None
        for student in faculty.students:
            if student.name == stud_name:
                naydennyy_student = student
                break
        if naydennyy_student is None:
           print("Студент не найден")
           continue
        with open("vedomost.txt", "w", encoding="utf-8") as file:
            file.write("Студент: " + naydennyy_student.name + "\n")
            file.write("Специальность: " + naydennyy_student.specialty + "\n")
            file.write("Дисциплины и оценки:\n")
            
            
            for discp in naydennyy_student.spisok_discp:
                ocenka = naydennyy_student.marks.get(discp.name, "нет оценки")
                file.write("  " + discp.name + " (кафедра: " + discp.kafedra.name + "): " + str(ocenka) + "\n")
            
            
            if len(naydennyy_student.marks) > 0:
                summa = 0
                for grade in naydennyy_student.marks.values():
                    summa = summa + grade
                sredniy = summa / len(naydennyy_student.marks)
                file.write("средний балл: " + str(sredniy) + "\n")
            else:
                file.write("средний балл: нет оценок\n")
        
        print("ведомость сохранена в файл vedomost.txt")  
    else:
        print("нет такого пункта")
        
