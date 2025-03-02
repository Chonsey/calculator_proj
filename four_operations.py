def sum_two_num(x, y):
    sum_nums = x + y 
    return sum_nums

def diff_two_num(num1, num2):
    diff_nums = num1 - num2 
    return diff_nums

def mult_two_num(num1, num2):
    mult_nums = num1 * num2 
    return mult_nums

def div_two_num(num1, num2):
    if num2 != 0:
        dive_nums = num1 / num2 
        return dive_nums
    error_massage = f"Не может быть осуществлено так как делимое равно {num2}"
    return error_massage


