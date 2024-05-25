#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 11
    while i > 0:
            i -= 1
            print(i)
    if i == 0:
         print('Happy New Year!')
happy_new_year()


def square_integers(int_list):
    # code goes here!
     int_list = [num ** 2 for num in int_list]
     return int_list

square_integers([1,2,4])

def fizzbuzz():
    # code goes here!
    for i in range(1,101):
         if i % 3 == 0 and i % 5 == 0:
              print('FizzBuzz')
         elif i % 5 == 0:
              print('Buzz')
         elif i % 3 == 0:
              print('Fizz')
         else:
              print(i)
fizzbuzz()