def binary(lst, findnumb):
    lst.sort()
    left = 0
    right = len(lst) - 1

    while left <= right:
        middle = (left + right) // 2
        if findnumb == lst[middle]:
            return middle
        elif findnumb < lst[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number_to_find = 5
result = binary(my_list, number_to_find)
if result != -1:
    print(f"Элемент {number_to_find} найден по индексу {result}")
else:
    print(f"Элемент {number_to_find} не найден в списке.")


if __name__ == '__main__':
    print(binary([1,2,3,4,6,1,3,2,5,7,8,0],5))

