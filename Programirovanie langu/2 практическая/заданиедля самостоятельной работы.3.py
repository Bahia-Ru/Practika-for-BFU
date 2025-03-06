from os.path import exists
import pickle

a = input('Введите слово для перевода: ')

def dictionary(lang,dict_dictionary):
    if lang not in dict_dictionary:
        diktobr = input('Я не знаю что такое:',lang,', подскажите пожалуйста:')
        dict_dictionary.setdefault(lang,diktobr)
        with open('dict_dictionary.pkl', 'wb') as f:
            pickle.dump(dict_dictionary, f)
    print(lang,'- это',dict_dictionary[lang])

def rfile():
    if exists('dict_dictionary.pkl') == False:
        dict_dictionary = dict({'cat' : 'кошка, кот','dog' : 'собака','home' : 'домашний каталог, дом','mouse' : 'мышь, манипулятор мышка','to do' : 'делать, изготавливать','to produce' : 'производить','sweet' : 'сладкий, милый','кошка':'cat','кот':'cat','собака':'dog','домашний каталог':'home','дом':'home','мышь':'mouse','манипулятор мышка':'mouse','делать':'to do','изготавливать':'to do','производить':'to produce','сладкий, милый':'sweet'})
        with open('dict_dictionary.pkl', 'wb') as f:
            pickle.dump(dict_dictionary, f)
    else:
        with open('dict_dictionary.pkl', 'rb') as f:
            dict_dictionary = pickle.load(f)
    return dict_dictionary

dict_dictionary = rfile()
dictionary(a,dict_dictionary)



 