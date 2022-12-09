input_string = input("Введите число")

def give_int_num(input_string: str) -> int:
    # input_string - предложение ввода
    # int - число

    while True:
        try:
            num = int(input(input_string))
            return num
        except ValueError:
            print("Неправильный ввод")