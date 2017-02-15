salary = 10000
save = 10
preRetireGrowthRates = [3, 4, 5, 0, 3]
postRetireGrowthRates = [10, 5, 0, 5, 1]
epsilon = .01

length = len(preRetireGrowthRates)
nestEgg = [salary * save * 0.01]

for i in range(1, length):
    nestEgg += [nestEgg[i - 1] * (preRetireGrowthRates[i] * 0.01 + 1) + nestEgg[0]]

##at this point i have savings at end of the pre-retirement period
##now i need to add the loop to guess within epsilon

savings = nestEgg[-1]
high = savings
low = 0
guess = (high + low) / 2
counter = 1

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

return a