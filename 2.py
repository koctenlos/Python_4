# Задайте два числа. 
# Напишите программу, которая найдет НОК 
# (наименьшее общее кратное) этих двух чисел. 
# НОК - наименьшее общее кратное, которое делится и 
# на первое, и на второе число.

a, b = map(int,input("Введите два числа через пробел: ").split())
def search_nod(a,b):
    while a!=0 and b!=0:
        if a>b:
            a = a%b
        else:  
            b = b%a
    return a+b
def search_nok(a,b,nod):
    return a*b/nod

print(search_nok(a,b,search_nod(a,b)))