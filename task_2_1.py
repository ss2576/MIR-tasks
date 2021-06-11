"""
У вас есть робот, который умеет взбираться вверх по лестнице с конечным количеством ступеней. Для этого вам
предоставляется низкоуровневая функцию step(), которая заставляет робота попытаться взобраться на 1 ступень
вверх. К сожалению, иногда у робота это не получается, и он вместо того чтобы взобраться на 1 ступень вверх, падает
и опускается на 1 ступень вниз от исходного положения (если ему есть куда опускаться). Робот определяет успешность
выполнения операции, и результат вам возвращается в качестве результата функции step(): 1 - успешно; 0 - не
успешно (падение).
Требуется написать функцию stepUp(N), которая приводит к тому, что робот поднимается ровно на 1 ступень вверх. N -
номер ступени, на которой находится робот в настоящий момент. Ступени нумеруются снизу вверх, начиная с единицы.
"""
import random


def step():
    random_number = random.randint(0, 2)
    if random_number == 0:  # если 0,то скатился
        count = 0
        steps = random.randint(0, 3)  # на какое кол-во ступеней скатился
    else:
        count = 1
        steps = 0
    return count, steps


def stepup(N):

    def func(n):
        count, steps = step()
        if count == 1:
            if n == N:
                print(f'робот поднялся на ступень №{n + 1}, подъем выполнен!')  # робот поднялся на заданную ступень N
            else:
                n += 1
                print(f'робот поднялся на ступень №{n}')
                func(n)
        else:
            if steps > n:
                print(f'робот скатился на ступень №{0}')  # робот скатился на нулевую ступень
                func(0)
            elif steps == 0:
                print(f'робот не смог подняться и остался на ступене №{n - steps}')  # робот остался на месте
                func(n)
            else:
                print(f'робот скатился на ступень №{n - steps}')  # робот скатился на steps кол-во ступеней назад
                func(n - steps)
    func(N)


if __name__ == '__main__':
    stepup(5)  # 5 - ступень, на которой стоит робот












