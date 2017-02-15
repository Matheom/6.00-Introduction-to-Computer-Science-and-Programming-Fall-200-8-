###
### template of code for Problem 4 of Problem Set 2, Fall 2008
###
#
# bestSoFar = 0     # variable that keeps track of largest number
#                   # of McNuggets that cannot be bought in exact quantity
# packages = (6,9,20)   # variable that contains package sizes
#
# for n in range(1, 150):   # only search for solutions up to size 150
#     ## complete code here to find largest size that cannot be bought
#     ## when done, your answer should be bound to bestSoFar

max_count = 50
packages = (6,9,20)
tu = ()
counter = 0

while counter < max_count:

    ans = 1
    counter += 1

    for a in range(0,counter):
        for b in range(0,counter):
            for c in range(0,counter):
                if a * packages[0] + b * packages[1] + c * packages[2] == counter:
                    ans = 0
    if ans == 1:
        tu += (counter,)

print(tu)



##############################
##internet solution to nugget problem

# def FindNuggetSolution (n):
#     for c in range (0, n):
#         for b in range (0, n):
#             for a in range (0, n):
#                 if (6*a + 9*b + 20*c == n):
#                      #PrintNuggetSolution (a, b, c, nuggets)
#                      return 1
#     return 0
#
# #looking for largest value of nuggest that cannot be bought in packs of 6, 9, and 20
# tu = ()
#
# for n in range(6,100):
#     if FindNuggetSolution(n) == 0:
#         tu += (n,)
#         nuggets = n
#
# print ("Largest number of McNuggets that cannot be bought in exact quantity:", nuggets )
# print(tu)
#
# def PrintNuggetFunction (nuggets):
#     print ('I want to order Chicken McNuggets in packs of 6, 9, and 20 so that I have exactly', nuggets, 'nuggets')
#     return
#
# def PrintNuggetSolution (a, b, c, nuggets):
#     print ('It takes', a, 'packs of 6,', b, 'packs of 9, and', c, 'packs of 20 Chicken McNuggets to =', nuggets)
#     return
#
# def FindNuggetSolution (nuggets):
#     for c in range (0, nuggets):
#         for b in range (0, nuggets):
#             for a in range (0, nuggets):
#                 if (6*a + 9*b + 20*c == nuggets):
#                      PrintNuggetSolution (a, b, c, nuggets)
#     return
#
# for i in range(50,65):
#     FindNuggetSolution(i)

################################################3
#my simplified version of internet solution


# def check(x):
#     for a in range(0,x):
#         for b in range(0,x):
#             for c in range(0,x):
#                 if a*6 + b*9 + c*20 == x:
#                     return 1
#     return 0
#
# for x in range(0,50):
#     if check(x) == 0:
#         print(x)


