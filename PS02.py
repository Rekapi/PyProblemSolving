# Continue
import math


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


# 44. how to solve (x + y) * (x + Y)
def solve_eq(a, b, c):
    x1 = float(((-b ** 2) + (math.sqrt((a ** 2) - 4 * a * c))) / (2 * a))
    x2 = float(((-b ** 2) - (math.sqrt((a ** 2) - 4 * a * c))) / (2 * a))
    return x1, x2


# 45. how to calculate the future value of rate of interest and a number of years
# 46. how to calculate the distance between two points
# 47. check if a file exists
# 48. check if python version is 64 or 32
# 49. check the os name, platform and release information
# 50. how to find the location of python site package directory
# 51. how to call an external command
# 52. how to get path and name of a file that currently executing in python
# 53. how to find out the number of CPUs
# 54. how to convert strings to float or int
# 55. how to print stderr
# 56. how to sort counter by value
# 57. converts height in feet and inches to centimeters
# 58. calculate the hypotenuse of a right angled triangle
# 59. how to get file creation & modification date times
# 60. calculate body mass index
# 61. converts seconds to day, hour, minutes and seconds
# 62. get a list of built in modules
# 63. how to find ASCII value of a character
# 64. remove the first item of a list
# 65. how to read the contents of an URL
# 66. how to get the system hostname
# 67. how to swap two variables
# 68. how to concatenate N strings
# 69. how to find file path or directory
# 70. how to get the users environment (77 in the PlayList)
