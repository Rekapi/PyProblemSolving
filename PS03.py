import itertools
# 89. print positive numbers in a list
nums = [34,35,1,0,-3, 5,-6,-7]
print("Example 89.")
print("------------")
print("original list : ", nums)
new_nums = list(filter(lambda x: x >0, nums))
print("Pos numbers : ", new_nums)
print("---------------------------------")

# 102. sum all the items in a list
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers

L = [1,2,4,5,9]
print("Example 102.")
print("------------")
print(sum_list(L))

# 103. remove duplicates on a list

# 104. clone a list

# 105. check if the list is empty

# 106. print all unique values in a dictionary

# 107. sort a dictionary by key

# 108. iterate over dictionaries using for loop

# 109. concatenate two dictionaries

# 114. flatten a shallow in a list

# 115. generate all permutations of a list
print("Example 115.")
print("------------")
print(list(itertools.permurarions(L)))

# 118. count number of Vowels in a string
# 120. create the HTML string with tags around the word
# 122. convert true to 1 and false to 0
# 123. printing dictionary in a table format
# 130. converting list into dictionary
# 135. select the odd items of a list
# 142. check if a python string starts with a specific character
# 149. run a shell command and get the output
# 151. get the command line arguments passed to a script
# 155. multiply all items in a dictionary
# 156. add all items in a dictionary
# 162. print yesterday ,today and tomorrow
# 174. convert a list into a nested dictionary of keys
# 177. sorting dictionary by values
# 178. find the depth of a dictionary
# 180. sort a list of nested dictionaries
# 182. get the number of days of a given month and year
# 188. find the length of a set
# 190. remove items from set
# 196. find the min max of values in a dictionary
# 202. shuffle and print a list
# 211. convert tuple to a dictionary
