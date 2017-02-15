

##problem 1



# def countSubStringMatch(target,key):
#
#     if int(str.find(target,key)) == -1:
#         print('there are no instances')
#
#     counter = 0
#
#     while int(str.find(target,key)) != -1:
#
#         if int(str.find(target, key)) >= 0:
#             counter += 1
#             a = int(str.find(target, key))
#             target = target[a+1:]
#
#
#     return counter
#
# print(countSubStringMatch('banana','a'))

# def countSubStringMatchRecursive(target,key):
#
#     a = int(str.find(target,key))
#
#     if a == -1:
#         return 0 #base case
#     elif a >= 0:
#         count = countSubStringMatchRecursive(target[a+1:],key) + 1
#         return count
#
#
# print(countSubStringMatchRecursive('banana','a'))


######################################################################################
################################### problem 2 ########################################


def subStringMatchExact(target, key):

    i = 0
    a = target.find(key,i)

    tu = [(a)]
    length = len(target)

    while (i + a) < length:

        b = target.find(key, i + a + 1)

        if b > 0:
            tu += [b]
        else:
            break
        i += b

    return tu



####note - i used 'target.find' as opposed to 'str.find'. I found the former more useful
#### since I dont have to reduce the length of the string to find the second 'key' - i
#### can simlpy tell it to start looking for the next 'key' after the 'nth' element
#### see example below

# target = 'bonana'
#
# b = target.find('a',4)
# c = str.find(target,'a')
#
# print(b)
# print(c)

###########################################################################################
##################################### problem 3 ###########################################

# target = 'bananaxn'
# key1 = 'na'
# key2 = 'n'
#
# match1 = (2,4)
# match2 = (2,4,7)
#
# tu = ()
#
#
# for a in range(len(match1)):
#     for b in range(len(match2)):
#
#         if match1[a] + len(key1) + 1 == match2[b]:
#             tu += (match1[a],)
#
# print(tu)

# def constrainedMatchPair(match1,match2,key1):
#
#     tu = ()
#     for a in range(len(match1)):
#         for b in range(len(match2)):
#
#             if match1[a] + len(key1) + 1 == match2[b]:
#                 tu += (match1[a],)
#
#     return tu

#################################################################################
#######################supplied code to test#####################################

# def subStringMatchOneSub(key, target):
#     """search for all locations of key in target, with one substitution"""
#     allAnswers = ()
#     for miss in range(0, len(key)):
#         # miss picks location for missing element
#         # key1 and key2 are substrings to match
#         key1 = key[:miss]
#         key2 = key[miss + 1:]
#         print('breaking key', key, 'into', key1, ' and ', key2)
#         # match1 and match2 are tuples of locations of start of matches
#         # for each substring in target
#         match1 = subStringMatchExact(target, key1)
#         match2 = subStringMatchExact(target, key2)
#         # when we get here, we have two tuples of start points
#         # need to filter pairs to decide which are correct
#         filtered = constrainedMatchPair(match1, match2, len(key1))
#         allAnswers = allAnswers + filtered
#         print('match1', match1)
#         print('match2', match2)
#         print('possible matches for', key1, key2, 'start at', filtered)
#     return allAnswers
#
# subStringMatchOneSub('ATGC', 'ATGACATGCA')
