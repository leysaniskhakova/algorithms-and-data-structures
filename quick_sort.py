
# быстрая сортировка для пустого массива или массива, содержащего один элемент
# базовый случай

def quicksort_base(array):
    if len(array) < 2:
        return array


# быстрая сортировка

def quicksort(array):
    if len(array) < 2:                                  # базовый случай: массивы с 0 и 1 элементами
        return array                                    # уже "отсортированы"
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]     # подмассив всех элементов, меньших опорного
        greater = [i for i in array[1:] if i > pivot]   # подмассив всех элементов, больше опорног0
    
    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))
