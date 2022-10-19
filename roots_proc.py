import sys
import math
from dataclasses import dataclass

@dataclass
class valid_of_coef:
    is_valid: bool
    coef: float

def is_coef_valid(coef_str):
    try:
        coef = float(coef_str)
        coef_to_retun = valid_of_coef(True, coef)
        return coef_to_retun
    except:
        coef_to_retun = valid_of_coef(False, 0)
        return coef_to_retun

def print_roots(roots) -> None:
    len_roots = len(roots)
    if len_roots == 0:
                print("Нет корней")
    else:
        string = "корня"
        if len_roots == 1:
            string = "корень"
        print("Уравнение имеет {} {}:".format(len_roots, string))
        print(roots)


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    # Переводим строку в действительное число
    coef = is_coef_valid(coef_str)
    while not (coef.is_valid):
        print(prompt)
        coef_str = input()
        coef = is_coef_valid(coef_str)
    return coef.coef


def get_roots(a, b, c):
    '''
    Вычисление корней биквадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = set()

    D = b*b - 4*a*c
    if D == 0.0:
        bi_root = -b / (2.0*a)
        root = math.sqrt(bi_root)
        result.add(root)
        result.add(-root)
        
    elif D > 0.0:
        sqD = math.sqrt(D)
        bi_root1 = (-b + sqD) / (2.0*a)
        bi_root2 = (-b - sqD) / (2.0*a)

        if bi_root1 >= 0:
            root1 = math.sqrt(bi_root1)
            result.add(-root1)
            result.add(root1)

        if bi_root2 >= 0:
            root2 = math.sqrt(bi_root2)
            result.add(-root2)
            result.add(root2)
   
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    try:
        roots = get_roots(a,b,c)
        # Вывод корней
        print_roots(roots)
    except ZeroDivisionError:
        print("Ошибка! Деление на 0!")
    except:
        print("Неизвестная ошибка")
    

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# roots_proc.py 1 0 -4