# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:26:38 2024

@author: Admin
"""

def fib_generator(num):
    '''
    this will works as generator function and take yield into account.
    '''
    assert num > 0
    a, b = 1, 1
    while num > 0:
        yield a
        a, b = b, a+b
        num -= 1


times = int(input('Enter the number for fib generaton: '))
fib_gen = fib_generator(times)
while(times > 0):
    print(next(fib_gen))
    times = times - 1