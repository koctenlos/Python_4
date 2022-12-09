# Задайте натуральное число N. 
# Напишите программу, которая составит список простых 
# множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

num = int(input("Введите число: "))
i = 2 #Prostoe chislo
alist = []
old = num
while i <= num:
    if num % i == 0:
        alist.append(i)
        num //= i
    else:
        i += 1
print(f"Простые множители {old} приведены в списке:  {alist}")
