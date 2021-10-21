import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    #try:
     #   # Пробуем прочитать коэффициент из командной строки
      #  coef_str = sys.argv[index]
    #except:
        # Вводим с клавиатуры
    while True:
        i = 0
        flag = True
        print(prompt)
        lst = input().split()
        num_list = list(map(str, lst))
        coef_str = num_list[len(num_list) - 1]
        for sym in coef_str:
            if sym == '-' and i == 0 and len(coef_str) > 1:
                continue
            if sym not in '0123456789':
                flag = False
                break
            i += 1
        if flag:
            break


    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''

    result = []
    if (a**2 + b**2) != 0:
        D = b * b - 4 * a * c
        if D == 0.0:
            root = -b / (2.0 * a)
            if root >= 0:
                result.append(abs(math.sqrt(root)))
                if root != 0.0:
                    result.append((-1)*abs(math.sqrt(root)))
        elif D > 0.0:
            sqD = math.sqrt(D)
            root1 = (-b + sqD) / (2.0 * a)
            root2 = (-b - sqD) / (2.0 * a)
            if root1 >= 0:
                result.append(abs(math.sqrt(root1)))
                if root1 != 0:
                    result.append((-1)*abs(math.sqrt(root1)))
            if root2 >= 0:
                result.append(abs(math.sqrt(root2)))
                if root2 != 0.0:
                    result.append((-1)*abs(math.sqrt(root2)))
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    while a == 0:
        a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {} и {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {} и {} и {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))
# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4
