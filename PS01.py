# 1. How to find average N numbers in python
"""num = int(input('How many numbers ?'))
total_sum = 0
for n in range(num):
    numbers = float(input('Enter any number'))
    total_sum += numbers
avg = total_sum / num
print('Average is :', avg)

# 2. How to Sum of the first N positive integers in Python
num = int(input('How many numbers ?'))
total_sum = 0
for n in range(num):
    numbers = float(input('Enter any number'))
    total_sum += numbers
Sum = total_sum
print('Average is :', Sum) """

# import cProfile
# 7. How to list all files of a directory
# from os import listdir
# from os.path import isfile, join
import datetime
import getpass
import os
# 3. How to get time of a python program's execution **
import time


def myFunc():
    start_time = time.time()
    s = 0
    for i in range(1, n + 1):
        s = s + i
    end_time = time.time()
    return s, end_time - start_time


n = 5
print(myFunc())

# 4. How to get the current user name in python


print(getpass.getuser())

# 5. How to access environment variables


print(os.environ['PATH'])

# 6. How to do a profile a python script


""" def add():
    print(1, 3)


cProfile.run('add()') """

# 7. How to list all files of a directory

# 8. find out the version of python you are using
""" print("Python system")
print(sys.version)
print(sys.version_info) """

# 9. print current time and date **
now = datetime.datetime.now()
print('current date and time :', now.strftime('%y-%m-%d %H:%M:%S'))
# 10. find area of a circle
"""r = float(input('Whats the radius of your circle : '))
area = pi * r ** 2
print('Area of the circle = ', area)"""

# 11. reverse a string
"""Str = input('whats your word ')
print(Str[::-1])"""  # reversing using slice

# 12. create a list and tuple with comma separated numbers
""" values = input('input some numbers')
Lst = values.split(",")
Tpl = tuple(Lst)
print('List : ', Lst)
print('Tuple : ', Tpl) """

# 13. extract extension from file name
""" file_Name = input('write the fileName')
file_ext = file_Name.split('.')
print(repr(file_ext[-1])) """

# 14. display the first and last colors from a given list in python
"""colors = ['blue', 'red', 'white', 'Black']
print('the first color is :' + colors[0] + colors[-1])"""
# 15. display a sample examination schedule

# 16. how to read a number b and compute n+nn+nnn
"""a = int(input('whats your number : '))
print(a + a * a + a * a * a) """

# 17. how to print the documents of python built in function

# 18. how to print a calendar for the given month and year **
""" y = int(input('Enter the year '))
m = int(input('Enter the month '))
print(calendar.month(y, m)) """

# 19. how to write string without having escape

# 20. how to calculate number of days between two dates ** calculate your age
"""firstDate = date(2019, 2, 2)
secondDate = date(2000, 4, 4)
delta = firstDate - secondDate
print(delta.days + 'days') """

# 21. how to find volume and surface area of sphere

# 22. how to find the difference between two numbers

# 23. calculate Sum of three numbers if the values are equal then return thrice of their Sum
"""n1 = int(input('Enter the first number '))
n2 = int(input('Enter the second number '))
n3 = int(input('Enter the third number '))
if n1 == n2 == n3:
    Sum = n1 + n2 + n3
    print(Sum*3)
else:
    print('the numbers is not equals')"""

# 24. how to get a new string from a given string

# 25. how to find whether an integer is even or odd number
num = int(input('Enter your number : '))
if num % 2 == 0:
    print('The number is even ')
else:
    print('the number is odd')
# 26. how to reverse a number using slice operation
print('reverse ' + str(num)[::-1])  # converting the number to string and reverse it

# 27. how to find the biggest and smallest of 3 numbers using list
num1 = 3
num2 = 4
num3 = 6
List = [num1, num2, num3]
print('the biggest number is ', max(List))
print('the smallest number is ', min(List))

# 28. calculate the Sum of elements in a list
print(sum(List))

# 29. how to find the area of triangle
a = float(input('the height is : '))
b = float(input('the base length is : '))
area = 0.50 * a * b
print('the area = ', area)
# 30. how to find the area of triangle given base and height

# 31. how to get a string which is n copies of a given string

# 32. how to count the number of items in a list # len(List)

# 33. find n copies of the first characters of a given string
u_input = input('enter your string ')
ch_count = 0
for char in u_input:
    if char == u_input[0]:
        ch_count += 1
print(ch_count)


# 34. how to check if item is in list or not **
def is_group_number(group_data, nom):
    for value in group_data:
        if nom == value:
            return True
    return False


print(is_group_number([1, 2, 3, 4, 5], 5))


# 35. how to create histogram from a given list of integers

# 36. how to turn a list into a string
def concat_list(lst):
    result = ''
    for element in lst:
        result += str(element)
    return result


print(concat_list(['m', 'a', 'h', 'm', 'o', 'u', 'd']))

# 37. how to print even numbers in the given range

Numero = int(input('how many number'))
for n in range(Numero):
    if n % 2 == 0:
        print(n)

# 38. how to compare lists
c1 = set(['black', 'white', 'blue', 'yellow'])
c2 = set(['magenta', 'purple', 'blue', 'yellow'])
print(c1.difference(c2))

# 39. how to find the greatest common divisor GCD in python

# 40. how to find least common multiple LCM
