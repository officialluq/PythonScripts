from numpy import random

x = random.randint(100, size=50)


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break

    return array

# def test(array):
#     count = len(array)
#     for i in range(count):
#         if()
#         array[i]



def teast():
    #input
    a = [2342, "dsfg"]
    correct = cerret_sotr

    #action
    result = bubble_sort(a)

    #test
    assert result == correct



print(f'Before {x}')
print(f'After {bubble_sort(x)}')
