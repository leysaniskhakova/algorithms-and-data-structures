
def binary_search(list, item):
    low = 0                      # В переменных low  и high хранятся границы той части списка,
    high = len(list)-1           # которой выполяентся поиск

    while low <= high:                  # пока эта часть не сократиться до одного элемента...
        mid = round((low + high)/2)     # ...проверяем средний элемент
        guess = list[mid]
        if guess == item:               # Занчение найдено
            return mid
        if guess > item:                # Много
            high = mid - 1
        else:                           # Мало
            low = mid + 1
    return None                         # Значение не существует

my_list = [1, 3, 5, 7, 9]               # тестируем функцию

print(binary_search(my_list, 3))  # 1
print(binary_search(my_list, -1)) # None