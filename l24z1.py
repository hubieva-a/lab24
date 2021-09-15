#!/usr/bin/env python3
# -*- config: utf-8 -*-

from threading import Thread, Lock
import math

x = 0.35
e = 2.71
y = math.log((math.sqrt((1 + x) / (1 - x))), e)

n = 1
x_sum = 0
x_element = 1
k = 1
t = 0.0000001
x_ls = []

while x_element >= t:

    def func_thread(n, x_sum):
        x_element = (x ** n) / n
        x_sum = x_sum + x_element
        x_ls.append(x_element)
        print(x_sum)
        return x_element, x_sum


    n = n + 2

    thread_list = []
    results = []

    for x in x_ls:
        thread = threading.Thread(target=func_thread, args=(x, results))
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()


def more_or_less():
    str1 = 'Сумма S больше Y  '
    str4 = 'Y больше суммы S  '
    str2 = 'S ='
    str3 = ' Y ='
    print(results)

    if x_sum > y:
        print(f"{str1}", f"{str2}", x_sum, f"{str3}", y)
    else:
        print(f"{str4}", f"{str2}", x_sum, f"{str3}", y)


if __name__ = '__main__':

    th2 = Thread(target=more_or_less)
    th2.join()



