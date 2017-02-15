# Problem Set 4
# Name:
# Collaborators:
# Time:

#
# Problem 1
#

# def nestEggFixed(salary, save, growthRate, years):
#
#     tu = []
#     tu2 = []
#
#     for i in range(years):
#
#         value = (salary * save * 0.01)*(1 + growthRate * 0.01)**(i)
#         tu.append(value)
#
#     for i in range(years + 1):
#
#         if i > 0:
#             tu2.append(sum(tu[0:i]))
#
#     return tu2
#
# def testNestEggFixed():
#     salary     = 10000
#     save       = 10  #multiply 0.01 to get %
#     growthRate = 15  #multiply 0.01 to get %
#     years      = 5
#
#     savingsRecord = nestEggFixed(salary, save, growthRate, years)
#
#     print(savingsRecord)
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

# testNestEggFixed()


# #
# # Problem 2
# #
#
# def nestEggVariable(salary, save, growthRates):
#     # TODO: Your code here.
#     """
#     - salary: the amount of money you make each year.
#     - save: the percent of your salary to save in the investment account each
#       year (an integer between 0 and 100).
#     - growthRate: a list of the annual percent increases in your investment
#       account (integers between 0 and 100).
#     - return: a list of your retirement account value at the end of each year.
#     """
#
#     length = len(growthRates)
#     nestEgg = [salary * save * 0.01]
#
#     for i in range(1,length):
#
#         nestEgg += [nestEgg[i-1] * (growthRates[i]*0.01 + 1) + nestEgg[0]]
#
#
#     return nestEgg
#
#
#
# def testNestEggVariable():
#     salary      = 10000
#     save        = 10
#     growthRates = [3, 4, 5, 0, 3]
#     savingsRecord = nestEggVariable(salary, save, growthRates)
#     print(savingsRecord)
#
# testNestEggVariable()

#     # Output should have values close to:
#     # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]
#
#     # TODO: Add more test cases here.
#
# #
# # Problem 3
# #
#
# def postRetirement(savings, growthRates, expenses):
#     """
#     - savings: the initial amount of money in your savings account.
#     - growthRate: a list of the annual percent increases in your investment
#       account (an integer between 0 and 100).
#     - expenses: the amount of money you plan to spend each year during
#       retirement.
#     - return: a list of your retirement account value at the end of each year.
#     """
#     # TODO: Your code here.
#
#     length = len(growthRates)
#     nestEgg = [savings * (growthRates[0] * 0.01 + 1) - expenses]
#
#     for i in range(1, length):
#         nestEgg += [nestEgg[i - 1] * (growthRates[i] * 0.01 + 1) - expenses]
#
#     return nestEgg
#
# def testPostRetirement():
#     savings     = 100000
#     growthRates = [10, 5, 0, 5, 1]
#     expenses    = 30000
#     savingsRecord = postRetirement(savings, growthRates, expenses)
#     print(savingsRecord)
#     # Output should have values close to:
#     # [80000.000000000015, 54000.000000000015, 24000.000000000015,
#     # -4799.9999999999854, -34847.999999999985]
# testPostRetirement()
#
#     # TODO: Add more test cases here.
#
# #
# # Problem 4

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    # TODO: Your code here.

    length = len(preRetireGrowthRates)
    nestEgg = [salary * save * 0.01]

    for i in range(1, length):
        nestEgg += [nestEgg[i - 1] * (preRetireGrowthRates[i] * 0.01 + 1) + nestEgg[0]]

    savings = nestEgg[-1] #this is the savings at end of retirement period

    #start bi-section method here - start guessing

    high = savings
    low = 0
    guess = (high + low) / 2
    a = 100

    while abs(a) > epsilon:

        length = len(postRetireGrowthRates)
        finalamount = [savings * (postRetireGrowthRates[0] * 0.01 + 1) - guess]

        for i in range(1, length):
            finalamount += [finalamount[i - 1] * (postRetireGrowthRates[i] * 0.01 + 1) - guess]

        if finalamount[-1] < 0:
            high = guess
        else:
            low = guess

        guess = (high + low) / 2
        a = finalamount[-1]

    return guess

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print(expenses)

testFindMaxExpenses()
#     # Output should have a value close to:
#     # 1229.95548986
#
#     # TODO: Add more test cases here.