"""Последовательность чисел Фибоначчи F(N) задаётся рекуррентным соотношением:
F(0) = 0;
F(1) = 1;
F(N) = F(N-1) + F(N-2), N>=2;
Требуется написать программу (на любом языке программирования), которая вычисляет N-ый элемент
последовательности.
 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711
                5                 10                     15                           20
 """
from time import time


def time_of_function(function):
    """декоратор подсеча времени выполнения функции"""
    def wrapped(*args):
        start_time = time()
        res = function(*args)
        end_time = time()
        print(f'time of calculation {function.__name__}:', end_time - start_time)
        return res
    return wrapped


# вариант 1. рекурсивный. сложность O(2^N)
@time_of_function
def fib_1(n):
    def func(m):
        if m < 2:
            return m
        return func(m - 1) + func(m - 2)
    print(f'вариант 1: {n}-е число в списке Фибоначчи равно {func(n)}')


# вариант 2. сложность O(N)
@time_of_function
def fib_2(n):
    if n < 2:
        return n
    pp = 0
    p = 1
    for i in range(n - 1):
        pp, p = p, pp + p
    print(f'вариант 2: {n}-е число в списке Фибоначчи равно {p}')


if __name__ == '__main__':
    number = 22
    fib_1(number)
    fib_2(number)





