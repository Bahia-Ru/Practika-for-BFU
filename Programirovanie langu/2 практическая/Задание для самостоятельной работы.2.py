from os.path import exists
import pickle

a = input('Введите язык: ')

def lang(Langua,dict_Langua):
    if Langua not in dict_Langua:
        country = input('Я не знаю где говорят на таком языке, подскажите пожалуйста: ')
        dict_Langua.setdefault(Langua,country)
        with open('dict_Langua.pkl', 'wb') as f:
            pickle.dump(dict_Langua, f)
    print("На",Langua,'говорят в',dict_Langua[Langua])

def rfile():
    if exists('dict_Langua.pkl') == False:
        dict_Langua = dict({'русский':'Россия','французский':'Франция','греческий':'Кипр', 'турецкий':'Кипр','английский': 'Сингапур', 'китайский': 'Сингапур', 'малайский': 'Сингапур'})
        with open('dict_Langua.pkl', 'wb') as f:
            pickle.dump(dict_Langua, f)
    else:
        with open('dict_Langua.pkl', 'rb') as f:
            dict_Langua = pickle.load(f)
    return dict_Langua

dict_Langua = rfile()
lang(a,dict_Langua)

# Россия              русский
# Франция             французский
# Кипр                греческий, турецкий
# Сингапур            английский, китайский, малайский