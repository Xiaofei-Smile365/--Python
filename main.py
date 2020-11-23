# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    n = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    sum = 0
    pi = 0

    for i in range(0 + 1, n + 1):
        sum = 1/(i * i) + sum
        pi = (sum * 6) ** 0.5
        print("The pi is %s in n = %s" % (pi, i))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
