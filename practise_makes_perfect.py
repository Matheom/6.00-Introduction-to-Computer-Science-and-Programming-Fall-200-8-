# print("please enter a string")
# response = str(input())
#
# print("please enter a number")
# response2 = int(input())

# print(response*response2)

#######my first function
# def cmp(x,y):
#
#     if x > y:
#         print(x, ' is greater than ',y)
#     elif x < y:
#         print(x, ' is less than ', y)
#     else:
#         print(x, ' and ', y, ' are the same')
#
# cmp(2,2)

# def countdown(n):
#     if n==0:
#         print('blast off!')
#     else:
#         print(n)
#         countdown(n-1)
#
# n = 10
#####gues the number game
# answer = 5
# question = 'guess what number i am thinking of BIATCH!!\n'
#
# print(question)
#
# while True:    #note - use the whie true if we want to continiously run throgh the loop
#     guess = int(input())
#
#     if guess < answer:
#         print('little higher')
#     elif guess > answer:
#         print('little lower')
#     else:
#         print('mindufkc!!')
#         break  #note - use break to end the loop once the partoiciapnt got the correct answer
###averagebetween 3 numbers
# x = int(input('first number?\n'))
# z = int(input('second number?\n'))
# y = int(input('third number?\n'))
#
# final = x+y+z
# print(final/3)

######################################
#IF EXCERCISES
#1 - password

# password = 'hello'
# g_count = 0
#
# while True:
#     guess = input('Please type in password\n')
#
#     if guess == password:
#         print('Password Correct')
#         break
#     else:
#         print('Incorrect password')
#         g_count = g_count + 1
#
#         if g_count == 3:
#             print('Password entered too many times')
#             break

#2 - sum of 2 number

# a = int(input('first number?\n'))
# b = int(input('second numer?\n'))
#
# if a + b > 100:
#     print('wow, that\'s a big number!')


#assignment 1 MIT CS 600
#
# candidate = 1
# nth_prime = 1000
# counter = 1
#
#
# while counter < nth_prime:
#
#     candidate = candidate + 2
#     divisor = 2
#     prime = 1
#
#     while divisor < candidate:
#         if candidate%divisor == 0:
#             prime = False
#         divisor = divisor +1
#
#     if prime == True:
#         counter = counter + 1
#
#         if counter == nth_prime:
#             print(candidate)
#             break
###assignment 2 MIT CS 600

# from math import *
#
# nth_prime = 1000
# counter = 1
# candidate = 1
# #mylist = []
# tu = ()
#
# while counter < nth_prime:
#
#     candidate = candidate + 2
#     prime = 1
#     divisor = 2
#
#     while divisor<candidate:
#         if candidate%divisor == 0:
#             prime = 0
#         divisor = divisor + 1
#
#     if prime == 1:
#         counter = counter+1
#         #mylist.append(candidate)
#         tu += (candidate,)
#         if counter == nth_prime:
#            #a = sum([log(i) for i in mylist])
#             a = sum([log(i) for i in tu])
#             b = a/candidate
#             print('The ', nth_prime, 'th prime is', candidate)
#             print(a)
#             print(b)
#
#             break

            #[math.log10(i) for i in mylist]
####lists
# squares = [x**2 for x in range(10)]
# print(squares)




# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
#
# for char in prefixes:
#     if char == 'O' or char == 'Q':
#         print(char + 'u' + suffix)
#     print(char + suffix)

# def threeLines():
#     newLine()
#     newLine()
#     newLine()
#

#
# def nineLines():
#     threeLines()
#     threeLines()
#     threeLines()
#
# print('first line')
# nineLines()
# print('second line')

import math
#
# def hypotenuse(x,y):
#     x2 = x**2
#     y2 = y**2
#     hypotenuse  = math.sqrt(x2+y2)
#     return hypotenuse
#
# print(hypotenuse(2,2))


# def mcNug(n):
#
#     packages = (6,9,20)
#
#     for a in range(0,n):
#         for b in range(0,n):
#             for c in range(0,n):
#                 if a*packages[0]+b*packages[1]+c*packages[2] == n:
#                     return 1
#     return 0
#
#
# for n in range(1,150):
#     if mcNug(n) == 0:
#         print(n)
#########3
#Fibonachi sequence
# x,y=0,1
#
# while y<50:
#     print(y)
#     x,y = y,x+y

# def fibonacci (n):
#   if n == 0 or n == 1:
#     return 1
#   else:
#     return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(12))


#########3excersice 10

# for x in range(0,50):
#
#     if x % 3 == 0:
#         print('Fizz')
#     if x % 5 == 0:
#         print('Buzz')
#     else:
#         print(x)

############EX.11

# from math import *
#
# candidate = 1
# counter = 1
# nth_prime = 1000
# tu = ()
#
# while counter < nth_prime:
#
#     candidate += 2
#     divisor = 2
#     prime = 1
#
#     while divisor < candidate:
#         if candidate % divisor == 0:
#             prime = 0
#         divisor += 1
#
#     if prime == 1:
#         counter += 1
#         tu += (candidate,)
#
#
#
# lgsum = sum([log(y) for y in tu])
# ratio = lgsum/candidate
#
# print(candidate)
# print(lgsum)
# print(ratio)

#
# from math import *
#
# nth_prime = 1000
# counter = 1
# candidate = 1
# #mylist = []
# tu = ()
#
# while counter < nth_prime:
#
#     candidate = candidate + 2
#     prime = 1
#     divisor = 2
#
#     while divisor<candidate:
#         if candidate%divisor == 0:
#             prime = 0
#         divisor = divisor + 1
#
#     if prime == 1:
#         counter = counter+1
#         #mylist.append(candidate)
#         tu += (candidate,)
#         if counter == nth_prime:
#            #a = sum([log(i) for i in mylist])
#             a = sum([log(i) for i in tu])
#             b = a/candidate
#             print('The ', nth_prime, 'th prime is', candidate)
#             print(a)
#             print(b)

###########assignment 3 MIT600  -MY OWN FUKEN SOLUTION FUCKA

# max_count = 50
# packages = (6,9,20)
# tu = ()
# counter = 0
#
# while counter < max_count:
#
#     ans = 1
#     counter += 1
#
#     for a in range(0,counter):
#         for b in range(0,counter):
#             for c in range(0,counter):
#                 if a * packages[0] + b * packages[1] + c * packages[2] == counter:
#                     ans = 0
#     if ans == 1:
#         tu += (counter,)
#
# print(tu)


########################################


# def fib(n):
#
#     if n==1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# fib(9)


# color = ['spam!', ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
#
#
# # for a in range(len(color)):
# #     print(len(color[a]))
#
# print(id(color))
###########################################

######dictionaries########################

previous = {0:1,1:1}

def fib(n):
    if n in previous:
        return previous[n]
    else:
        newValue = fib(n-1) + fib(n-2)
        previous[n] = newValue
        return newValue

print(fib(38))

for a,b in previous.items():
    print(a,b)


















