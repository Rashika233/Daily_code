#map_filter codde
'''
num=[1,2,3,4,5,6,7,8,9,10]
l1=map(lambda x: x**2, filter(lambda x:x%2==0, num))
print(list(l1))'''

'''import functools
import operator
List_2d=[[1,2,3],[4,5],[6,7,8]] 
List_flat = functools.reduce(operator.iconcat, List_2D, [])
print('original list:', List_2d)
print('flattened list:', List_flat)'''


#flateing a list using reduce function
'''import functools
import operator

List_2D = [[1,2,3],[4,5,6],[7,8,9]] #List to be flattened

List_flat = functools.reduce(operator.iconcat, List_2D, [])

print("Original List:",List_2D)
print("Flattened List:",List_flat)'''


#flatening a list using itertools

'''import itertools
list_2D=[[1,2,3],[4,5,6],[7,8,9]]
list_flat=list(itertools.chain(*list_2D))
print('The original_list is :', list_2D)
print('The flattened_list is :', list_flat)'''


#flatening using nested list
'''
List_2D = [[1,2,3],[4,5,6],[7,8,9]] #List to be flattened
List_flat = []

for i in range (len(List_2D)):
     for j in range (len(List_2D[i])):
        List_flat.append(List_2D[i][j])
print('original list:', List_2D)
print('flattened list:', List_flat)'''   

# a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)

'''tup1= (1,2,3,4,5,6,7,8,9,10)
tup2=list() #taking empty list to store the result values
for i in range(len(tup1)):
    if tup1[i]%2==0:
        tup2.append(tup1[i])
    else:
        pass
tup3=tuple(tup2)
print(tup3)'''

# a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10]

'''list1=[1,2,3,4,5,6,7,8,9,10]
list2=map(lambda x:x**2,list1)
print(list(list2))'''

'''
l1=map(lambda x:x%3, range(50))
print(list(l1))'''

#program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
'''
l1=filter(lambda x: x%2==0, range(21))
print(list(l1))'''

#reverse a string
'''
txt='1234abcd'
print(txt[::-1])'''

#reversing a string using functn
''''def rev_str(txt):
    return txt[::-1]

print(rev_str('1234abcd'))'''

# a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
''''
def txt(string):
    low=0
    up=0
    for i in string:
        if i.islower()==True:
            low+=1
        else:
            up+=1
    return (low,up)
print(txt('URITGkhvjvkv'))'''

#returning a unique list
def uni(list):
    l1=[]
    for i in list:
        if i not in l1:
            l1.append(i)
    return l1
print(uni([1,23,4,5,5,5,6,7,7,7,8,9,9])) 