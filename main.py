from four_operations import sum_two_num, div_two_num, diff_two_num, mult_two_num





user_res = input("че ты хочешь вычислить милорд ? ")
user_res_lower = user_res.lower()
if user_res_lower == "сложить":
    num1 = int(input('Введи первое число: '))
    num2 = int(input('Введи второое число: '))
    print(f'Сумма твоих чисел равна {sum_two_num(x=num1,y=num2)}')
if user_res_lower == "вычесть":
    num1 = int(input('Введи первое число: '))
    num2 = int(input('Введи второое число: '))
    print(f'Разница твоих чисел равна {diff_two_num(num1=num1,num2=num2)}')
if user_res_lower == "умножить":
    num1 = int(input('Введи первое число: '))
    num2 = int(input('Введи второое число: '))
    print(f'произведение твоих чисел равна {mult_two_num(num1=num1,num2=num2)}')
if user_res_lower == "разделить":
    num1 = int(input('Введи первое число: '))
    num2 = int(input('Введи второое число: '))
    print(f'деление {num1} на {num2}: {div_two_num(num1=num1,num2=num2)}')








