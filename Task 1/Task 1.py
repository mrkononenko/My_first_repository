import re
import sys
def find_str(find_str, method):
    if method == 0:
        integer_stroka = re.findall(r'\d+', find_str)
        integer_stroka = [int(i) for i in integer_stroka]
        return integer_stroka
    elif method == 1:
        string_stroka = re.findall(r'\D', find_str)
        string_stroka = [str(i) for i in string_stroka]
        string_stroka = ''.join(string_stroka)
        return string_stroka
    else:
        return "Виникла помилка!"

def Degree(integer_stroka):
    maxi = max(integer_stroka)

    res = []
    for i in range(len(integer_stroka)):
        if integer_stroka[i] != maxi:
            res.append(integer_stroka[i]**(i+1))

    return res

def BigLetters(string_stroka):
    res = ""
    k = 0
    spl = str(string_stroka).split()
    for i in spl:
        for i in spl[k].split():
            a = ''.join(spl[k])
            if len(a) == 1:
                res += a[0].upper()+' '
            else:
                res += a[0].upper()+a[1:-1]+a[-1].upper() + ' '
            k += 1
    return res

stroka = input("Введіть рядок:\n")
print("Ваш рядок:", stroka)
integer_stroka = find_str(stroka, 0)
print("Рядок із цифрами:\n", integer_stroka)
string_stroka = find_str(stroka, 1)
print("Максимальне значення в рядку : \n", max(integer_stroka))
print("Рядок зі степенем масива чисел\n", Degree(integer_stroka))
print("Рядок із символами:\n", string_stroka)
print("Рядок із великими буквами по краям:\n", BigLetters(string_stroka))