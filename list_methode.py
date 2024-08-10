'''
list is mutable - elements can be added ,removed and
updated from the list

add element in list
1)append(): this method adds elements at the end of the list
syntax: list_variable.append(value)
2)insert(index,value): this method is used to add element in
            particular position

syntax: list_variable.insert(index,value)


l1=[10,'Roshan',45.26,'Agre']
print(l1)

l1.append(20)
print(l1)

l1.insert(1,'Online-Class')
print(l1)

l2=[45,'Vidhati',6,'Agre']
print('list 2:',l2)

r=l1+l2
print(r)


l1.extend(l2)
print(l1)

l1.append(20)
print(l1)


#updating an element

l1=[10,'Roshan',45.26,'Agre']
print(l1)
l1[2]=60.7
print(l1)

pop():this method always delete last element from the list
pop(index):this delete particular element from the list


l1.pop()
print(l1)
l1.pop(2)
print(l1)


#del==> this will delete the list

del l1
#print(l1)
'''

mylist=[12,45,26,2,15,58,50]
print(mylist)
mylist.reverse()
print(mylist)

print('Min Number:',min(mylist))
print('Max Number:',max(mylist))
print('Sum of numbres:',sum(mylist))

mylist.sort()   #asc
print(mylist)
mylist.sort(reverse=True)   #dec
print(mylist)










