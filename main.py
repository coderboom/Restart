# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import keyword
from keyword import kwlist
import sys


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(keyword.kwlist)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # _input = input('\n\n按下 enter 键后退出。')
    # print_hi(_input)
    for i in sys.argv:
        print(i)
    print('python`s locad is ', sys.path)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
