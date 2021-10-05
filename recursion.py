
def countdown(i):
    print(i)
    if i <= 1:             # Базовый случай
        return i
    else:
        countdown(i-1)     # Рекурсивный случай

countdown(3)


def greet(name):
    print('hello, ' + name + '!')
    greet2(name)
    print( 'getting ready to say bye...')
    bye()

def greet2(name):
    print('how are you, ' + name + '?')

def bye():
    print('ok bye!')

greet('maggie')


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(3))



# суммирование циклом
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(sum([2, 4, 6]))

# суммирование рекурсией
def recursion_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + recursion_sum(arr[1:])

print(recursion_sum([2, 4, 6]))

# рекурсивная функция для подсчета элементов в списке
def count(list):
    if len(list) == 0:
        return 0
    return 1 + count(list[1:])

print(count([2, 4, 6]))

# наибольшее число в списке
def max_number(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max_number(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(max_number([2, 4, 6]))