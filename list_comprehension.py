'''
list comprehension
- list comprehension is used to create new list from
other iterable

'''
mylist=[10,20,30,40,50]
'''
mylist2=[]
for x in mylist:
    mylist2.append(x)

print(mylist2)
'''

mylist2=[i for i in mylist]
print(mylist2)

#new list which is containing square of each element
mylist3=[i*i for i in mylist]
print(mylist3)


#even number from 1 to 20 => if x%2==0
mylist3=[x for x in range(1,20) if x%2==0]
print(mylist3) #2,4,6,...18

#1 to 10
n=int(input("Enter number:")) #10
s=0
for i in range(1,n+1):
    s=s+i
print(s)
