
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def sort_list_deklarative(num):
    n = len(num)
    for i in range(n):
        for j in range(0, n - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num

def sort_list_imper(num):
    return sorted(num)
    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
   print(sort_list_deklarative([3,1,2,5]))
   print(sort_list_imper([3,1,2,5]))

