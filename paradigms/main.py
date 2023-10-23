
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
def multiply(nubmer):
    step = 1
    while step <= nubmer:
        print("{} * {} = ".format(step,nubmer) + str(  step*nubmer))
        step+=1

if __name__ == '__main__':

   multiply(5)
