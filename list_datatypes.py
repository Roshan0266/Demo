'''
list:
- it is enclosed in square brackets
- it is containing elements of different datatypes
- it is mutable


l1=[10,'Roshan',45.26,'Agre']
print(l1)
dt=type(l1)
print(dt)

#accessing list element(index)


        [10,'Roshan',45.26,'Agre']
positive  0     1       2      3
negative  -4   -3       -2     -1

syntax: list_variable[index]


x=l1[1]
print(x)
print(l1[-1])

#len()-> no. of elements

n=len(l1)
print('No. of elements:',n)

#for loop over list

for x in l1:
    print(x)

print('---------')
for x in range(0,len(l1)):
    #print(x)
    print(l1[x])

'''

l1=[10,'Roshan',45.26,'Agre']

#slicing=> list_variable[start:stop:step]

l2=l1[1:3:1]
print(l2)

l3=l1[::1]
print(l3)

l4=l1[::-1]  #[::-1] will give reverse list
print(l4)

l5=l1[-1:-4:-1]
print(l5)
