'''
1. Выполнить задание уровня ultra-light
2. Написать декоратор, замеряющий время выполнение декорируемой функции.
3. Сравнить время создания генератора и списка с элементами: натуральные числа
от 1 до 1000000 (создание объектов оформить в виде функций).
'''
import time

def getTime(f):
    def wrapper( *args, **wargs ):
        t1 = time.perf_counter()

        f(*args, **wargs )

        t2 = time.perf_counter()
        print( 'Функция ',f.__name__,"- Время работы: ",t2-t1)
    return wrapper

@getTime
def getList(n):
    lst = [x for x in range(1, n+1 )]
    return lst

@getTime
def getGenList(n):
    for x in range(1, n + 1):
        yield x

getList(1000000)
getGenList(1000000)
