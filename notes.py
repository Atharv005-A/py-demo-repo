"""
In Python, a list is a built-in data structure used to store multiple values 
in a single variable. 
Lists are ordered, mutable (changeable), and allow duplicate elements.

Characteristics of Python Lists
    Ordered (elements have index positions)
    Mutable (elements can be changed)   / List as a dynamic array
    Allows duplicate values
    Can store different data types      / Heterogeneous elements
    Rference-based storage
    Indexing starts from 0 (positive & negative)
    List can store another list


Mutable Objects
Mutable objects can be changed after they are created. This means their content (values)
can be modified without changing their identity (memory address).

Immutable Objects
Immutable objects cannot be changed after creation. If any modification is attempted,
a new object is created instead.

Key Differences:    Mutable                     vs          Immutable
Feature	            Mutable Objects (Can Change)	        Immutable Objects (Cannot Change)
Modification	    Allowed	                                Not Allowed
Memory Usage	    Can change in place	                    New object is created on change
Examples	        List, Dictionary, Set, Bytearray	    Int, Float, String, Tuple, Frozen Set
"""



##Here's how you can work with lists in Python:
# a=10
# b=20
# c=a+b
# print(c)

# l1 = [1 , 4.5, 'code' , True ]
# print(l1)
# print(l1[1])

# l2 = [1,2,3,4,5,6]
# print(l2)
# print(type(l2))


#nested list
# l3 = [1,2,3,4,[5,6,7]]
# print(l3)
# for i in l3:
#     print(i)

#----------------------------------------------------------------
# #list operations
# l1=[1,2,3,4]
# l2=[5,6,7,8]

# l3=l1+l2    # it will concatenate 2 list
# print(l3)

# l4=l1*3     # list is stored 3 times in l4
# print(l4)

#-------------------------------------------------------------
## List methods

# lst = [10, 20, 30, 20, 40]
# print("Original List:", lst)

# # # 1. Insertion / Addition Methods
# #     append() – Add element at the end
# #     insert() – Add element at specific index
# #     extend() – Add multiple elements at end

# lst.append(50)
# print("After append(50):", lst)

# lst.insert(2, 25)
# print("After insert(2, 25):", lst)

# lst.extend([60, 70, 30])
# print("After extend([60, 70]):", lst)

## 2. Deletion / Removal Methods
#     remove(element) – Remove given element (first occurance only)
#     pop() – Remove last element
#     pop(index) – Remove element at index
#     clear() – Remove all elements

# lst = [10, 20, 30, 20, 40]
# lst.remove(20)
# print("After remove(20):", lst)

# lst.pop()
# print("After pop():", lst)

# lst.pop(1)
# print("After pop(1):", lst)

# lst.clear()
# print(lst)

# temp = lst.copy()
# temp.clear()
# print("After clear():", temp)

# del lst
# print(lst)

# # 3. Search / Information Methods
#     index() – Find index of element
#     count() – Count occurrences

# lst = [10, 20, 30, 20, 40]
# print("Index of 30:", lst.index(20))

# print("Count of 20:", lst.count(20))

# # 4. Rearrangement Methods
#     sort() – Sort list
#     sort(reverse=True) – Sort descending
#     reverse() – Reverse list

# lst = [10, 20, 30, 20, 40]
# lst.sort()
# print("After sort():", lst)

# lst.reverse()
# print("After reverse():", lst)

# lst.sort()
# lst.reverse()
# print(lst)

# lst.sort(reverse=True)
# print("After sort(reverse=True):", lst)


# # 5. Copy Methods
#     copy() – Shallow copy

# list1 = [1,2,3,4]
# list2 = list1       # method 1
# list2.append(5)
# print(list1)
# print(list2)
# print("id of list1:",id(list1))
# print("id of list2:",id(list2))

#    deepcopy
# list1 = [1,2,3,4]
# list2=list1.copy()  
# list2.append(5)
# print(list1)
# print(list2)
# print("id of list1:",id(list1))
# print("id of list2:",id(list2))


# #6. Built-in aggrigate Functions Used with Lists
#     len() - find length of elements
#     max() - find highest element
#     min() - find lowest element
#     sum() - find sum of all elements

# lst = [1,2,3,4,5]
# print("Length:", len(lst))

# print("Max:", max(lst))
# print("Min:", min(lst))

# print("Sum:", sum(lst))

# #7. Membership Operators
# print(30 in lst)
# print(100 not in lst)



########################################################################################
#multidimentional list ---> list having another list --> matrix, tabular 

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#     ]

# print(matrix)
# print(matrix[0])
# print(matrix[1][1])

# for row in matrix:
#     for val in row:
#         print(val, end=" ")
#     print()

# students = [
#     ["amit",78,86.2],
#     ["akash",80,80.20],
#     ["vishwajeet",86,92.50]
# ]

# print(students)

# for student in students:
#     print("Name:",student[0],"Marks:",student[1],",",student[2])
    
# data = [
#     [1,2],
#     [3,4]
# ]
# data.append([5,6])
# print(data)

# wap to add all elements in multi. dimentional list
# data = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# tot=0
# for row in data:
#     for val in row:
#         tot+=val

# print("Total is:",tot)


#  find max element in multi. dimentional list
# matrix = [
#     [8,7,6],
#     [5,9,2],
#     [2,10,8]
# ]

# max=0
# for row in matrix:
#     for val in row:
#         if val>max:
#             max=val
# print("Max is:",max)

# wap to count total row and columns
# matrix = [
#     [1,2,3],
#     [4,5,6]
# ]

# print("row count is:",len(matrix))
# print("column count is:",len(matrix[0]))

"""
    A                   B
    1   2   3           10  20  30          11  22  33 
    4   5   6       +   40  50  60   =      44  55  66
    7   8   9           70  80  90          77  88  99

"""


# a = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# b = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# c = [
#     [0,0,0],
#     [0,0,0],
#     [0,0,0]
# ]

# # addition
# for i in range(3):
#     for j in range(3):
#         c[i][j] = a[i][j]+b[i][j]


# for i in range(3):
#     for j in range(3):
#         print(c[i][j], end=" ")
#     print()

# # multiplication
# for i in range(3):
#     for j in range(3):
#         c[i][j]=0
#         for k in range(3):
#             c[i][j] = a[i][k]*b[k][j]

# for i in range(3):
#     for j in range(3):
#         print(c[i][j], end=" ")
#     print()




#####################################################################################

# List Comprehension
    # List comprehension is a concise and readable way to create lists in Python. 
    # It allows you to generate a new list by applying an expression to each item in an 
    # iterable (such as a list, tuple, or range), optionally with conditions.
    # In simple terms, it is a compact replacement for loops used to build lists.

# Basic Syntax
# new_list = [expression for item in iterable]

# l=[]
# for i in range(1,6):
#     l.append(i)
# print(l)

# l=[i for i in range(1,11)]
# print(l)

# l=[i for i in range(1,51) if i%2==0]
# print(l)

# l=[n*n for n in range(1,11)]
# print(l)


# 1. Create a list of cube of numbers from 1 to 10
# l=[n*n*n for n in range(1,11)]
# print(l)

# 2. Create a list of odd numbers from 1 to 20

# l=[i for i in range(1,20) if i%2!=0]
# print(l)

# 3. Create a list of odd numbers from an existing list 

# lst=[1,2,3,4,5,6,7,8,9,10]
# l=[ i for i in lst if i%2!=0]
# print(l)

# 4. Convert a list of strings into uppercase
# str = "code and cad it"
# ucase = [ch.upper() for ch in str]
# print(ucase)

# 5. Create a list of lengths of each word in a sentence
# str = "code and cad it"
# wordlength = [len(word) for word in str.split()]
# print(wordlength)

# 6. Replace negative numbers with 0
# lst = [1,-2,6,8,-3,7,-5]
# new_lst =[i if i>0 else 0 for i in lst  ]
# print(new_lst)

# 7. Create a list of numbers divisible by both 3 and 5 (1–100)
# lst = [i for i in range(1,101) if i%3==0 and i%5==0]
# print(lst)

# 8. Extract vowels from a string
# str = "code and cad it"
# new_str=[i for i in str if i in "aeiou"]
# print(new_str)


# -------------------------------------------
# Write a Python program to create a list of integers and display all its elements.
# Write a Python program to find the sum of all elements in a given list.
# Write a Python program to find the largest element in a list.
# Write a Python program to count how many even numbers are present in a list.
# Write a Python program to reverse a given list.
# Write a Python program to search for a given element in a list and display whether it is found or not.
# Write a Python program to create a two-dimensional list (matrix) and display it.
# Write a Python program to access and display a specific element from a two-dimensional list.
# Write a Python program to generate a list of squares of numbers from 1 to 10 using list comprehension.
# Write a Python program to create a new list containing only even numbers from an existing list using list comprehension.

# Write a Python program to remove duplicate elements from a list without using built-in set functions.
# Write a Python program to find the second largest element in a list.
# Write a Python program to merge two lists into a single list without duplicate elements.
# Write a Python program to perform addition of two matrices using two-dimensional lists.
# Write a Python program to find the transpose of a given matrix.
# Write a Python program to calculate and display the sum of each row in a two-dimensional list.
# Write a Python program to convert a two-dimensional list into a one-dimensional list.
# Write a Python program to generate a multiplication table (1 to 10) using list comprehension.
# Write a Python program to find common elements between two given lists.
# Write a Python program to generate a list of prime numbers within a given range using list comprehension.

# # 1. Create a list of integers and display all elements
# lst = [10, 20, 30, 40, 50]
# for i in lst:
#     print(i)

# # 2. Find the sum of all elements in a list
# lst = [10, 20, 30, 40]
# total = 0
# for i in lst:
#     total += i
# print("Sum =", total)

# # 3. Find the largest element in a list
# lst = [12, 45, 7, 89, 23]
# largest = lst[0]

# for i in lst:
#     if i > largest:
#         largest = i

# print("Largest =", largest)

# # 4. Count even numbers in a list
# lst = [10, 15, 20, 25, 30]
# count = 0

# for i in lst:
#     if i % 2 == 0:
#         count += 1

# print("Even numbers =", count)

# # 5. Reverse a list
# lst = [1, 2, 3, 4, 5]
# rev = []

# for i in range(len(lst)-1, -1, -1):
#     rev.append(lst[i])

# print(rev)

# # 6. Search for an element in a list
# lst = [5, 10, 15, 20]
# key = 15

# found = False
# for i in lst:
#     if i == key:
#         found = True

# if found:
#     print("Element found")
# else:
#     print("Element not found")

# # 7. Create and display a two-dimensional list (matrix)
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:
#     print(row)

# # 8. Access a specific element from a 2D list
# matrix = [[10, 20], [30, 40]]
# print(matrix[1][0])   # Output: 30

# # 9. Squares from 1 to 10 using list comprehension
# squares = [i*i for i in range(1, 11)]
# print(squares)

# # 10. Even numbers using list comprehension
# lst = [1, 2, 3, 4, 5, 6]
# even = [i for i in lst if i % 2 == 0]
# print(even)

# # 11. Remove duplicates without using set
# lst = [1, 2, 2, 3, 4, 4, 5]
# unique = []

# for i in lst:
#     if i not in unique:
#         unique.append(i)

# print(unique)

# # 12. Find the second largest element
# lst = [10, 40, 30, 20]
# largest = second = -999

# for i in lst:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i > second and i != largest:
#         second = i

# print("Second largest =", second)

# # 13. Merge two lists without duplicates
# a = [1, 2, 3]
# b = [3, 4, 5]
# merged = []

# for i in a + b:
#     if i not in merged:
#         merged.append(i)

# print(merged)

# # 14. Addition of two matrices
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]
# result = [[0, 0], [0, 0]]

# for i in range(2):
#     for j in range(2):
#         result[i][j] = A[i][j] + B[i][j]

# print(result)

# # 15. Transpose of a matrix
# matrix = [[1, 2, 3], [4, 5, 6]]
# transpose = []

# for i in range(3):
#     row = []
#     for j in range(2):
#         row.append(matrix[j][i])
#     transpose.append(row)

# print(transpose)

# # 16. Sum of each row in a 2D list
# matrix = [[1, 2], [3, 4], [5, 6]]

# for row in matrix:
#     print("Row sum =", sum(row))

# # 17. Convert 2D list to 1D list
# matrix = [[1, 2], [3, 4], [5, 6]]
# one_d = []

# for row in matrix:
#     for i in row:
#         one_d.append(i)

# print(one_d)

# # 18. Multiplication table (1 to 10) using list comprehension
# table = [i*j for i in range(1, 11) for j in range(1, 11)]
# print(table)

# # 19. Find common elements between two lists
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]

# common = [i for i in a if i in b]
# print(common)

# # 20. Prime numbers in a range using list comprehension
# primes = [n for n in range(2, 51)
#           if all(n % i != 0 for i in range(2, n))]

# print(primes)

#####################################################################################
#tuple
# 1. Introduction to Tuple (Theory)
#     A tuple is a built-in data type in Python used to store a collection of elements in 
#     a single variable.Tuples are ordered, immutable, and allow heterogeneous data 
#     (different data types).

# Definition 
# A tuple is an ordered and immutable collection of elements enclosed in parentheses () and separated by commas.

# Syntax
# tuple_name = (element1, element2, element3, ...)

# 2. Characteristics of Tuple
# Ordered – Elements have a fixed index
# Immutable – Elements cannot be modified after creation
# Allows duplicate values
# Supports multiple data types
# Faster than lists
# Uses less memory than lists

# ------------------------------------------------------------------------
# # Creating a Simple Tuple
# t = (10, 20, 30)
# print(t)
# print(type(t))

# # Tuple with Different Data Types
# t = (1, "Python", 3.5, True)
# print(t)

# # Single Element Tuple
# # Comma is mandatory
# t = (5,)
# print(t)
# print(type(t))

# # Tuple without Parentheses
# t = 1, 2, 3
# print(t)

# # Accessing Tuple Elements
# # Using Indexing
# t = (10, 20, 30, 40)
# print(t[0])
# print(t[-1])

# # Using Slicing
# print(t[1:3])

# # Tuple Immutability
# # Tuples cannot be modified after creation.
# t = (10, 20, 30)
# t[0] = 100   # Error

# # -------------------------------------------------------------
# # Tuple Operations

# # Concatenation
# t1 = (1, 2)
# t2 = (3, 4)
# t3 = t1 + t2
# print(t3)

# # Repetition
# t = (1, 2)
# print(t * 3)

# # Membership Operator
# t = (10, 20, 30)
# print(20 in t)

# # -----------------------------------------------------------

# # Tuple Methods
# # Tuples support only two methods:

# # count()
# t = (1, 2, 2, 3)
# print(t.count(2))

# # index()
# print(t.index(3))

# # Tuple Packing and Unpacking
# # Packing
# t = 10, 20, 30
# print(t)

# # Unpacking
# a, b, c = t
# print(a, b, c)

# # Nested Tuples
# t = (1, (2, 3), 4)
# print(t[1][0])

# wap to store details of student
# stu = ("suraj",1,86,28,"sangli")
# print(stu)

# wap find length of tuple
# t=(1,5,3,6,8,6,5,2,4,6)
# print("length of tuple is:",len(t))

# wap find max and min in tuple
# t=(1,5,9,6,7,5,26,984,2,3,6,4,0)
# print("Max is:",max(t),"\tMin is:",min(t))

# wap to convert list into tuple and viceversa
# l = [1,2,3,4]
# t=tuple(l)
# print(t)
# print(type(t))

# t1 = (4,5,6,7)
# l1 = list(t1)
# print(l1)
# print(type(l1))



# Practice Programs
# Write a program to create a tuple and display its elements.
# Write a program to access the first and last element of a tuple.
# Write a program to find the length of a tuple.
# Write a program to check whether an element exists in a tuple.
# Write a program to find the maximum and minimum elements in a tuple.
# Write a program to count the occurrence of an element in a tuple.
# Write a program to perform tuple unpacking.
# Write a program to create a nested tuple and access its elements.
# Write a program to concatenate two tuples.







#####################################################################################
# # Sets in Python
# # A set in Python is an unordered, mutable collection of unique elements. 
# # Sets are commonly used when you need to store distinct values and perform 
# # mathematical set operations such as union, intersection, and difference.
# # or tasks that involve storing and manipulating collections of unique elements.

# # Key Characteristics of Sets
# # Unordered: Elements do not have a fixed position or index.
# # Unique elements only: Duplicate values are automatically removed.
# # Mutable: You can add or remove elements after creation.
# # Heterogeneous: A set can store different data types.


# # Creating a set
# # Using curly braces
# s1 = {10, 20, 30, 40}

# # Using set() constructor
# s2 = set([1, 2, 3, 4])

# print(s1)
# print(type(s1))
# print(s2)

# # creating empty set
# empty_set = set()

# # Accessing Set Elements
# # You cannot access elements using index. Use loops.

# s = {10, 20, 30, 40, 50, 60, 70, 80, 90}
# for x in s:
#     print(x)


# # Adding Elements
# s = {10, 20, 20}
# s.add(30)          # add single element
# s.update([40, 50]) # add multiple elements
# s.add(30)
# print(s)

# # Removing Elements
# s = {10, 20, 30}
# s.remove(20)   # error if element not found
# s.discard(40)  # no error if element not found
# s.pop()        # removes random element
# s.clear()      # removes all elements
# print(s)

# # Set Operations 
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print(a | b)   # Union --> concatenate using unique values
# print(a & b)   # Intersection --> gives common elements
# print(a - b)   # Difference --> gives you unique value from set a
# print(a ^ b)   # Symmetric Difference --> gives you unique value from both set()

# # Set Membership
# s = {10, 20, 30}
# print(20 in s)      # True
# print(50 not in s)  # True

# # Built-in Set Functions
# s = {1, 2, 3, 4}
# print(len(s))   # number of elements
# print(max(s))
# print(min(s))
# print(sum(s))


# # Frozenset (Immutable Set)
# fs = frozenset([1, 2, 3])
# print(fs)
# fs.add(4)  # Error: frozenset is immutable

# practice program on set
# # Create a set and display all its elements.
# # Add a single element to an existing set.
# # Add multiple elements to a set using update().
# # Remove a specified element from a set.
# # Remove an element safely using discard().
# # Find the total number of elements in a set.
# # Check whether a given element exists in a set.
# # Remove duplicate elements from a list using a set.
# # Create an empty set and insert elements into it.
# # Find the maximum and minimum element from a set.

# # Find the union of two sets.
# # Find the intersection of two sets.
# # Find the difference between two sets.
# # Find the symmetric difference between two sets.
# # Check whether one set is a subset of another.
# # Check whether one set is a superset of another.
# # Find common elements between two lists using sets.
# # Remove all common elements from two sets.
# # Count the number of unique words in a given sentence using a set.
# # Demonstrate the use of frozenset in a program.


# # 1. Create a set and display all elements
# s = {10, 20, 30, 40}
# print("Set elements:")
# for x in s:
#     print(x)

# # 2. Add an element to a set
# s = {1, 2, 3}
# s.add(4)
# print(s)

# # 3. Add multiple elements to a set
# s = {10, 20}
# s.update([30, 40, 50])
# print(s)

# # 4. Remove an element from a set
# s = {10, 20, 30}
# s.remove(20)
# print(s)

# # 5. Remove an element without error
# s = {1, 2, 3}
# s.discard(5)
# print(s)

# # 6. Find the length of a set
# s = {10, 20, 30, 40}
# print("Length:", len(s))

# # 7. Check element existence in set
# s = {10, 20, 30}
# print(20 in s)

# # 8. Remove duplicate values from list using set
# lst = [1, 2, 2, 3, 4, 4]
# unique = set(lst)
# print(unique)

# # 9. Create an empty set
# s = set()
# s.add(10)
# s.add(20)
# print(s)

# # 10. Find maximum and minimum element
# s = {5, 10, 15, 20}
# print("Max:", max(s))
# print("Min:", min(s))

# # 11. Union of two sets
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b)

# # 12. Intersection of two sets
# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a & b)

# # 13. Difference of two sets
# a = {1, 2, 3, 4}
# b = {3, 4}
# print(a - b)

# # 14. Symmetric difference
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a ^ b)

# # 15. Check subset
# a = {1, 2}
# b = {1, 2, 3, 4}
# print(a.issubset(b))

# # 16. Check superset
# a = {1, 2, 3, 4}
# b = {2, 3}
# print(a.issuperset(b))

# # 17. Find common elements in two lists
# l1 = [1, 2, 3, 4]
# l2 = [3, 4, 5, 6]
# common = set(l1) & set(l2)
# print(common)

# # 18. Remove common elements from two sets
# a = {1, 2, 3, 4}
# b = {3, 4, 5}
# a.difference_update(b)
# print(a)

# # 19. Count unique words in a sentence
# sentence = "python is easy and python is powerful"
# words = set(sentence.split())
# print("Unique words count:", len(words))

# # 20. Use frozenset as dictionary key
# fs = frozenset([1, 2, 3])
# d = {fs: "Immutable Set"}
# print(d)


###############################################################################################################
# # Dictionary in Python
# # In Python, a dictionary is a mutable, unordered (insertion-ordered since Python 3.7+)
# # collection of data that stores elements in key–value pairs.

# # Key Characteristics of Dictionaries

# # Stores data as {key: value}
# # Keys must be unique
# # Keys are immutable (int, float, string, tuple)
# # Values can be any data type (int, list, tuple, dict, etc.)
# # Mutable → can be changed after creation

# student = {
#     "name": "Amit",
#     "roll": 101,
#     "marks": 85.5
# }

# print(student)
# ------------------------------------------

# # Using dict() Constructor
person = dict(name="Rahul", age=22, city="Pune")
# print(person)
# print(type(person))

# ----------------------------------------------

# # Accessing Dictionary Elements
# student = {
#     "name": "Amit",
#     "roll": 101,
#     "marks": 85.5
# }
# # Using Key
# print(student["name"])
# print(student["marks"])
# print(student["city"])  #keyerror

# # Raises KeyError if key does not exist.

# # Using get() Method (Safe)
# print(student.get("marks"))
# print(student.get("grade", "Key Not Found"))

# ----------------------------------------------------
# # Adding and Updating Elements
# student = {
#     "name": "Amit",
#     "roll": 101,
#     "marks": 85.5
# }
# # Add New Key-Value Pair
# student["grade"] = "A"
# print(student)

# # Update Existing Value
# student["marks"] = 90
# print(student)
# ---------------------------------------------------

# # Dictionary Methods (Important)
# # Method	            Purpose
# # keys()	            Returns all keys
# # values()	        Returns all values
# # items()	            Returns key–value pairs

# student = {
#     "name": "Amit",
#     "roll": 101,
#     "marks": 85.5
# }

# print(student.keys())
# print(student.values())
# print(student.items())
# -----------------------------------------------------

# # Looping Through a Dictionary
# # Loop Through Keys
# student = {
#     "name": "Amit",
#     "roll": 101,
#     "marks": 85.5
# }

# for key in student:
#     print(key)

# # Loop Through Values
# for value in student.values():
#     print(value)

# # Loop Through Key–Value Pairs
# for k, v in student.items():
#     print(k, ":", v)

# --------------------------------------------------
# # Nested Dictionaries
# # A dictionary inside another dictionary.

# students = {
#     101: {"name": "Amit", "marks": 80},
#     102: {"name": "Neha", "marks": 90}
# }

# print(students[101])
# print(students[101]["name"])

# practice program dictonary
# Write a Python program to create a dictionary with 5 key–value pairs and display it.
# Write a program to access the value of a given key from a dictionary.
# Write a program to add a new key–value pair to an existing dictionary.
# Write a program to update the value of an existing key in a dictionary.
# Write a program to delete a key–value pair from a dictionary using del.
# Write a program to check whether a given key exists in a dictionary or not.
# Write a program to print all keys of a dictionary.
# Write a program to print all values of a dictionary.
# Write a program to iterate through a dictionary and print keys and values separately.
# Write a program to find the length (number of key–value pairs) of a dictionary.

# Write a Python program to count the frequency of each character in a given string using a dictionary.
# Write a program to count the frequency of elements in a given list using a dictionary.
# Write a program to merge two dictionaries into a single dictionary.
# Write a program to find the key with the maximum value in a dictionary.
# Write a program to find the key with the minimum value in a dictionary.
# Write a program to sort a dictionary by keys.
# Write a program to sort a dictionary by values.
# Write a program to create a dictionary using dictionary comprehension where keys are numbers from 1 to 10 and values are their squares.
# Write a program to create a nested dictionary to store student details (roll number, name, marks) and display them.
# Write a program to remove duplicate values from a dictionary.

# -----------------------------------------------------------------------
# Basic Level Solutions (1–10)
# 1. Create a dictionary with 5 key–value pairs
# student = {
#     "name": "Amit",
#     "roll": 101,
#     "branch": "CSE",
#     "marks": 85,
#     "city": "Pune"
# }
# print(student)

# 2. Access the value of a given key
# print(student["name"])

# 3. Add a new key–value pair
# student["grade"] = "A"
# print(student)

# 4. Update the value of an existing key
# student["marks"] = 90
# print(student)

# 5. Delete a key–value pair using del
# del student["city"]
# print(student)

# 6. Check whether a key exists
# key = "roll"

# if key in student:
#     print("Key exists")
# else:
#     print("Key does not exist")

# 7. Print all keys
# print(student.keys())

# 8. Print all values
# print(student.values())

# 9. Iterate and print keys and values
# for key, value in student.items():
#     print(key, ":", value)

# 10. Find the length of a dictionary
# print("Total elements:", len(student))

# 🔹 Moderate Level Solutions (11–20)
# 11. Character frequency in a string
# text = "banana"
# freq = {}

# for ch in text:
#     freq[ch] = freq.get(ch, 0) + 1

# print(freq)

# 12. Frequency of elements in a list
# lst = [1, 2, 2, 3, 3, 3, 4]
# freq = {}

# for item in lst:
#     freq[item] = freq.get(item, 0) + 1

# print(freq)

# 13. Merge two dictionaries
# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}

# d1.update(d2)
# print(d1)

# # 14. Key with maximum value
# data = {"a": 10, "b": 50, "c": 30}

# max_key = max(data, key=data.get)
# print("Max value key:", max_key)

# # 15. Key with minimum value
# min_key = min(data, key=data.get)
# print("Min value key:", min_key)

# # 16. Sort dictionary by keys
# data = {"c": 3, "a": 1, "b": 2}

# sorted_dict = dict(sorted(data.items()))
# print(sorted_dict)

# # 17. Sort dictionary by values
# sorted_dict = dict(sorted(data.items(), key=lambda x: x[1]))
# print(sorted_dict)

# # 18. Dictionary comprehension (1–10 squares)
# squares = {x: x*x for x in range(1, 11)}
# print(squares)

# # 19. Nested dictionary (student details)
# students = {
#     101: {"name": "Amit", "marks": 80},
#     102: {"name": "Neha", "marks": 90}
# }

# for roll, details in students.items():
#     print(roll, ":", details)

# # 20. Remove duplicate values from dictionary
# data = {"a": 1, "b": 2, "c": 1, "d": 3}
# result = {}

# for key, value in data.items():
#     if value not in result.values():
#         result[key] = value

# print(result)


# ===================================== Map filter reduce =============================================



# List Creation and Display
# Create a list of 5 integers entered by the user and display the list.

# Sum of List Elements
# Write a program to find the sum of all elements in a given list.

# Find Maximum and Minimum
# Given a list of numbers, find the maximum and minimum elements without using built-in functions.

# Count Even and Odd Numbers
# Write a program to count how many even and odd numbers are present in a list.

# Search an Element
# Given a list and a number, check whether the number exists in the list.

# Reverse a List
# Reverse a given list without using the reverse() method.

# List Length Calculation
# Find the length of a list without using the len() function.

# Remove an Element
# Remove a specified element from a list and display the updated list.

# Copy a List
# Create a copy of a given list and verify that both lists are different objects.

# Display Elements Using Loop
# Print all elements of a list using a for loop and index positions.


# Remove Duplicate Elements
# Write a program to remove duplicate elements from a list without using set().

# Second Largest Element
# Find the second largest element in a list of integers.

# List Rotation
# Rotate the elements of a list to the right by k positions.

# Frequency Count
# Count the frequency of each element in a list and display the result.

# Merge and Sort Lists
# Merge two lists and sort the resulting list without using sort().

# Split List into Even and Odd Lists
# Given a list of integers, create two separate lists: one for even numbers and one for odd numbers.

# Matrix Representation Using Lists
# Accept a 2D list (matrix) and find the sum of all elements.

# Demonstrate shallow copy behavior using a nested list and explain the output.

# Implement stack operations (push, pop, display) using a Python list.
# Given a list containing numbers from 1 to n with one missing number, find the missing number.

"""
1. Create and Display a List
Problem: Create a list of 5 integers and display it.

lst = [10, 20, 30, 40, 50]
print(lst)

2. Sum of List Elements
Problem: Find the sum of all elements in a list.

lst = [10, 20, 30, 40]
total = 0
for x in lst:
    total += x
print("Sum:", total)

3. Find Maximum and Minimum
Problem: Find max and min without built-in functions.

lst = [45, 12, 78, 34, 89]
max_val = min_val = lst[0]

for x in lst:
    if x > max_val:
        max_val = x
    if x < min_val:
        min_val = x

print("Max:", max_val)
print("Min:", min_val)

4. Count Even and Odd Numbers
lst = [1, 2, 3, 4, 5, 6]
even = odd = 0

for x in lst:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)

5. Search an Element
lst = [10, 20, 30, 40]
key = 30

found = False
for x in lst:
    if x == key:
        found = True
        break

print("Found" if found else "Not Found")

6. Reverse a List (Without reverse())
lst = [1, 2, 3, 4]
rev = []

for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])

print(rev)

7. Find Length Without len()
lst = [10, 20, 30, 40]
count = 0

for _ in lst:
    count += 1

print("Length:", count)

8. Remove an Element
lst = [10, 20, 30, 40]
lst.remove(30)
print(lst)

9. Copy a List
a = [1, 2, 3]
b = a.copy()

print(a, b)
print(id(a) == id(b))   # False

10. Display Elements with Index
lst = [100, 200, 300]

for i in range(len(lst)):
    print("Index:", i, "Value:", lst[i])


1. Remove Duplicates (Without set)
lst = [1, 2, 2, 3, 4, 4]
unique = []

for x in lst:
    if x not in unique:
        unique.append(x)

print(unique)

2. Second Largest Element
lst = [10, 50, 30, 40]
largest = second = -1

for x in lst:
    if x > largest:
        second = largest
        largest = x
    elif x > second and x != largest:
        second = x

print("Second Largest:", second)

3. Rotate List Right by k Positions
lst = [1, 2, 3, 4, 5]
k = 2

for _ in range(k):
    lst.insert(0, lst.pop())

print(lst)

4. Frequency Count
lst = [1, 2, 2, 3, 3, 3]
freq = {}

for x in lst:
    freq[x] = freq.get(x, 0) + 1

print(freq)

5. Merge and Sort Two Lists
a = [3, 1, 5]
b = [2, 4, 6]
merged = a + b

for i in range(len(merged)):
    for j in range(i+1, len(merged)):
        if merged[i] > merged[j]:
            merged[i], merged[j] = merged[j], merged[i]

print(merged)

6. Split Even and Odd Lists
lst = [1, 2, 3, 4, 5, 6]
even, odd = [], []

for x in lst:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print("Even:", even)
print("Odd:", odd)

7. Sum of Matrix Elements (2D List)
matrix = [[1, 2], [3, 4]]
total = 0

for row in matrix:
    for x in row:
        total += x

print("Sum:", total)

8. Shallow Copy Demonstration
a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(99)
print(a)
print(b)

9. Stack Implementation Using List
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack.pop())
print(stack)

10. Find Missing Number (1 to n)
lst = [1, 2, 4, 5]
n = 5

expected_sum = n * (n + 1) // 2
actual_sum = sum(lst)

print("Missing Number:", expected_sum - actual_sum)
"""


# 1. Count Occurrence of Each Element
# num = [1,2,2,2,3,3]
# lst = []
# for n in num:
#     if n not in lst:
#         print(n, ":", num.count(n))
#         lst.append(n)

# 2. Remove All Occurrences of a Given Element
# num = [1,2,3,4,2,3,5]
# while 2 in num:
#     num.remove(2)
# print(num)

# 3. Find Second Largest Element
# num = [1,3,5,2,6,7,2]
# num.sort()
# print(num[-2])

# 4. Rotate List to the Left by One Position
# num = [1,2,3,4,5]
# first=num.pop(0)
# num.append(first)
# print(num)


# 5. Rotate List to the Right by One Position
# num = [1,2,3,4,5]
# last=num.pop()
# num.insert(0,last)
# print(num)

# 6. Check if List is Sorted
# num = [1,3,5,4,2]       
# num.sort()
# for i in range(len(num)-1):
#     if num[i] <= num[i+1]:
#         sorted = True
#     else:
#         sorted = False
#         break

# if sorted == True:
#     print("List is Sorted")
# else:
#     print("list is not sorted")

# 7. Replace Negative Numbers with Zero
# num = [ 1, -2 , 3, -5, 3 ,-2]
# for i in range(len(num)):
#     if num[i]<0:
#         num[i]=0
# print(num)

# 8. Separate Prime and Non-Prime Numbers
# 9. Find Missing Number from a Sequence
# 10. Reverse List Without Using reverse()

