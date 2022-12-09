# Шифр Цезаря - это способ шифрования, где каждая буква 
# смещается на определенное количество символов влево 
# или вправо. При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - 
# сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - 
# сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в 
# файл шифрованный текст, а также функцию, которая 
# спрашивает ключ, считывает текст и дешифровывает его.

import string

def give_int_num(input_string: str) -> int:
    # input_string - предложение ввода
    # int - число

    while True:
        try:
            num = int(input(input_string))
            return num
        except ValueError:
            print("Неправильный ввод")

def get_encript_text(alphabet: str, text: str, key: int) -> str:
    # alphabet - алфавит учавствующий в шифровании
    # text - строка подлежащая шифрованию
    # key - 
    #  str - зашифрованная строка

    en_text = ""
    alphabet_long = len(alphabet)
    for simbol in text:
        i=0
        for s in alphabet:
            if simbol == s:
                index = i + key
            i += 1
        if index > alphabet_long:
            index -= alphabet_long
        en_text += alphabet[index]
    return en_text

def get_decript_text(alphabet: str, text: str, key: int) -> str:
     # alphabet - алфавит учавствующий в шифровании
    # text - строка подлежащая шифрованию
    # key - 
    #  str - зашифрованная строка
    de_text = ""
    alphabet_long = len(alphabet)
    for simbol in text:
        i = 0
        for s in alphabet:
            if simbol == s:
                index = i - key
            i += 1
        if index < 0:
            index - alphabet_long + index
        if index >= alphabet_long:
            index = index - alphabet_long
        de_text += alphabet[index]
    return de_text

alphabet = string.punctuation + string.ascii_letters
initial_text = "Шифр цезаря - это способ шифрования, где каждая буква смещается на определённое колличество символов"
key = 5

en_text = get_encript_text(alphabet, initial_text, key)
file_encript = open("encript.txt","w")
file_encript.write(en_text) #записываем зашифрованный файл
file_encript.close()

print("Текст зашифрован в encript")
key = give_int_num("Введите ключ дешифрования(вправо +, влево -)")


