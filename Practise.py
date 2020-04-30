# python file for messing around with python

## list, mutable
#list = [1, 2, 3, 4, 5]

## tuple, immutable
#tup = (21, 36, 14, 25, 39)
# fetch value from tuple
#print("tuple: ",tup[1])

## set, won't maintain sequence and can't have duplicates
#s = {32, 19, 48, 3, 21}
#print("set: ",s)


## dictionary
#data = {1:'Navin', 2:'Kiran', 4:'Harsh'}

# merge keys and values into dictionary
keys = ['Navin', 'Kiran', 'Harsh']
values = ['Python', 'Java', 'JS']
data = dict(zip(keys, values))
print(data)