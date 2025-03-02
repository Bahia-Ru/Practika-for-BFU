#A = {1,2,3}
#A = set('qwerty')
#print(A)

#A = {1,2,3}
#B = {3,2,3,1}
#print(A==B)

#A = set('Hello World')
#print(A)

#primes = {2,3,5,7,11}
#for num in primes:
#    print(num)

#A = {1,2,3}
#print(A)
#print(1 in A, 4 not in A)
#A.add(4)
#print(A)

#Контрольные задания:

#1
# A = set(input('Введите первое множество'))
# B = set(input('Введите второе множество'))
# C = set(A.intersection(B))
# c = len(C)
# print('Совпадений:',c)

#2
# A = set(input('Введите первое множество А:'))
# B = set(input('Введите второе множество В:'))
# raznostAB = set(A.difference(B))
# obedinenieAB = set(A.union(B))
# print('Разность множеств А-В:',raznostAB,'\n','Обьединение множеств А и В',obedinenieAB)

# #3
# section1 = {"Tom","Bob","Alice", "Tommy"}
# section2 = {"Alice","Bob","Andy", "Tom", "Mikky"}

#3.1

# srazu_v_2 = section1.intersection(section2)
# lensrazu = len(srazu_2)
# print('Людей участвующих сразу в 2-х секциях:',lensrazu,'\n','Люди участвующие сразу в 2-х секциях',srazu_2)

#3.2

# vsego_sports = section1.union(section2)
# col_vo = len(vsego_sports)
# print('Всего спротом занимаеться:',col_vo,'\n','Имена спортсменов:',vsego_sports)

#3.3

# podmnozhestvo_A_in_B = section1.issubset(section2)
# podmnozhestvo_B_in_A = section1.issuperset(section2)
# if podmnozhestvo_A_in_B==True:
#     print('Секция 1 это подмножество Секции 2')
# else: print('Секция 1 это не подмножество Секции 2')
# if podmnozhestvo_B_in_A==True:
#       print('Секция 2 это подмножество Секции 1')
# else: print('Секция 2 это не подмножество Секции 1')

#4
# section1 = {'Беляев','Клочкова','Лосев','Свиридова','Баранов'} #Физика и химия
# section2 = {'Степанов','Клочкова','Свиридова','Конев','Лосев'} #Математика и програмирование

# vsego_Docladov = len(section1) + len(section2)
# seccii= 2
# Spisok_uch = section1.union(section2)
# colvo_uch = len(Spisok_uch)
# Spisok_uch_v_2 = section1.intersection(section2)
# colvo_uch_v_2 = len(Spisok_uch_v_2)
# tolko_v_1 = section1.symmetric_difference(section2)
# colvo_uch_v_1 = len(tolko_v_1)

# print('Сколько всего докладов на конференции:',vsego_Docladov,'n','Сколько секций на конференции',seccii,'/n','')
# print('Список и количество участников конференции',colvo_uch,'Имена',Spisok_uch)
# print('Список и количество участников конференции, задействованных в обеих секциях',colvo_uch_v_2,'Имена',Spisok_uch_v_2 )
# print('Список и количество студентов, участвующих только в одной секции.',colvo_uch_v_1,'Имена',tolko_v_1)




