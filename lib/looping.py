#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10;
    while i > 0:
        print(i)
        i -= 1
    print('Happy New Year!')


def square_integers(int_list):
    # code goes here!
    squared_list= list()
    for i in int_list:
        square_integers = i*i
        squared_list.append(square_integers)
    return squared_list
        

def fizzbuzz():
    # code goes here!
    for i in range(1,101):
        if i % 5 == 0 and i % 3 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)
# print(fizzbuzz())


def reverse_string(str):
    reversed_string = ''
    for i in str:
        reversed_string = i + reversed_string
        print(reversed_string)
    return reversed_string
print(reverse_string('Tyler'))
