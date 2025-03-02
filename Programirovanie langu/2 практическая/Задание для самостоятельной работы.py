from os import *
dict_for_country = dict({'Москва':'Россия','Париж':'Франция','Лион':'Франция','Калининград':'Россия','Минск':'Беларусь'})
if path.exists('dict_for_country.txt')== False:
    # with open('dict_for_country.txt', 'w+') as openFile:
    #     openFile.write(dict_for_country)
    #     openFile.closed
    openFile = open('dict_for_country.txt','w+')
    openFile.write(set('dict_for_country'))
with open('dict_for_country.txt', 'r') as openFile:
    dict_for_country=openFile.readline()

   



# def cityes(city):
#     dict_for_country = dict({'Москва':'Россия','Париж':'Франция','Лион':'Франция','Калининград':'Россия','Минск':'Беларусь'})
#     if city in dict_for_country:
#         print(city,'Калининград- это',dict_for_country[city])
#     else:
#        country = input('Я не знаю где находится где находится такой город подскажите пожалуйста:')
#        dict_for_country.setdefault(city,country)

#     print(city,'- это',dict_for_country[city])


# a = input('введите название города:')
# if 1==1: 
    # cityes(a)


# Город        Страна
# Москва       Россия
# Париж        Франция
# Лион         Франция
# Калининград  Россия
# Минск        Беларусь