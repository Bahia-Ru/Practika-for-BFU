from numpy import *
alf = '0123456789АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪ'
text = '123'
k = [[0,36,17],
     [1,2,5],
     [9,13,11]]
x = -14
print('Исходящее сообщение:'+ '\n',text)
print('\n' + 'Ключ' + '\n', k)
print('\n' +'Шифрование:' )
text_num = []
for i in text:
    text_num.append(alf.find(i))

print('\n' + 'Закодированное исходное сообщение:' + '\n', text_num)
z_text_n = []
for i in range(0,len(text),3):   
    for str_num in range(len(k)):
        sum = 0
        for stlb_num in range(len(k)):
            if stlb_num + i < len(text_num):
                sum += text_num[stlb_num + i] * k[str_num][stlb_num]
        z_text_n.append(sum%37)  
print('\n' + "Закодированное зашифрованное сообщение:" + '\n', z_text_n)
z_text = ''
for i in z_text_n:
    z_text += alf[i]
print('\n' + 'Зашифрованное сообщение (По Алгоритму Хилла):' + '\n', z_text)
print('\n' + 'Расшифрование:')
det_k = round(linalg.det(k))
print('\n' + 'Детерминант ключа:' + '\n', det_k)
if det_k >= 0 and x>=0: x = x
elif det_k < 0 and x>= 0 : x= -x
elif det_k >= 0 and x< 0: x = 37 + x
elif det_k < 0 and x < 0: x=-x
print('\n' + 'Обратный детерминанту элемент x' + '\n', x)
obr_k = (linalg.inv(k) * det_k)%37 * x%37
print('\n' + 'Обратный матрица ключа:' + '\n', obr_k)
text_n = []
for i in range(0, len(z_text_n),3):
    for str_num in range(len(obr_k)):
        sum = 0
        for stlb_num in range(len(obr_k)):
            sum += z_text_n[stlb_num + i] * obr_k[str_num][stlb_num]
        text_n.append(round(sum%37))
print('\n' + 'Закодированное Расшифрованное сообщение:' + '\n', text_n)

ras_text = ''
for i in text_n:
    ras_text += alf[int(i)]
print('\n' + 'Расшифрованное сообщение:' + '\n', ras_text)