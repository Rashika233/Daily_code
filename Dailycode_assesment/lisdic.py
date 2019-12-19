test_dict={'gfg':[1,2], 'is':[3,4], 'here':[4,5]}
print('The original dictionary is : ' + str(test_dict))
res = [[i for i in test_dict[x]] for x in test_dict.keys()] 
print('The list values of keys are : ' + str(res))