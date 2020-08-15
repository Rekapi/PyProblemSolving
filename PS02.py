# Continue
from __future__ import print_function
import sys
import math
import textwrap
import http.client


# 41. how to Sum two given numbers and return a number (functions)
def summation(x, y):
    suma = x + y
    if suma in range(15, 20):
        return 20
    else:
        return suma


print(summation(2, 2))


# 42. how to add two objects if both objects are an integer type
def add_number(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Must be Integer")
    return a + b


print(add_number(1, 1))


# 43. how to display name, age, address in three different lines
def personal_detail():
    name, age = "mahmoud", 20
    address = "El Shrouk city "
    print("Name : {}\nage: {}\naddress: {}".format(name, age, address))


personal_detail()


# 44. how to solve quadratic equation
def solve_eq(a, b, c):
    y = b ** 2 - 4 * a * c
    z = 2 * a
    x1 = (-b + (math.sqrt(y)))
    x2 = (-b - (math.sqrt(y)))
    return x1 / z, x2 / z


"""a1 = float(input("The value of a : "))
b1 = float(input("The value of b : "))
c1 = float(input("The value of c : "))"""

print("(x1, x2) =", solve_eq(1, 5, 6))

# 45. how to calculate the future value of rate of interest and a number of years

# 46. how to calculate the distance between two points
p1 = [4, 0]
p2 = [6, 8]
distance = math.sqrt(((p1[0] - p2[0]) ** 2 + ((p1[1] - p2[1]) ** 2)))
print(distance)

# 47. check if a file exists
# 48. check if python version is 64 or 32
# 49. check the os name, platform and release information
# 50. how to find the location of python site package directory
# 51. how to call an external command
# 52. how to get path and name of a file that currently executing in python
# 53. how to find out the number of CPUs
# 54. how to convert strings to float or int
n = "244.3"
print(float(n))
print(int(float(n)))


# 55. how to print stderr
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


eprint("abc", "efg", "xyz", sep="__")

# 56. how to sort counter by value

# 57. converts height in feet and inches to centimeters

# 58. calculate the hypotenuse of a right angled triangle
# 59. how to get file creation & modification date times
# 60. calculate body mass index
# 61. converts seconds to day, hour, minutes and seconds

# 62. get a list of built in modules
module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))

# 63. how to find ASCII value of a character
# 64. remove the first item of a list

# 65. how to read the contents of an URL
conn = http.client.HTTPConnection("www.google.com")
conn.request("GET", "/")
result = conn.getresponse()
contents = result.read()
print(contents)

# 66. how to get the system hostname
# 67. how to swap two variables
# 68. how to concatenate N strings
# 69. how to find file path or directory
# 70. how to get the users environment (77 in the PlayList)
