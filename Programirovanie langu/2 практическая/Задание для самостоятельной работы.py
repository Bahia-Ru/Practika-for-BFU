from os.path import exists
import pickle

a = input('введите название города: ')

def cityes(city,dict_for_country):
    if city not in dict_for_country:
        country = input('Я не знаю где находится где находится такой город подскажите пожалуйста:')
        dict_for_country.setdefault(city,country)
        with open('dict_for_country.pkl', 'wb') as f:
            pickle.dump(dict_for_country, f)
    print(city,'- это',dict_for_country[city])

def rfile():
    if exists('dict_for_country.pkl') == False:
        dict_for_country = dict({'Москва':'Россия','Париж':'Франция','Лион':'Франция','Калининград':'Россия','Минск':'Беларусь'})
        with open('dict_for_country.pkl', 'wb') as f:
            pickle.dump(dict_for_country, f)
    else:
        with open('dict_for_country.pkl', 'rb') as f:
            dict_for_country = pickle.load(f)
    return dict_for_country

dict_for_country = rfile()
cityes(a,dict_for_country)