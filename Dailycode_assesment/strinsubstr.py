from itertools import combinations
str1='abababa'
print('The original string is :' + str(str1))
res=[str1[x:y] for x,y in combinations(range(len(str1)+1), r = 2)] 
print('All substrings of string are : ' + str(res))
