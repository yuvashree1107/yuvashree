'''a=[1,2,5,7,4,9,8,10]
 
even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers are" ,odd)
print("Odd numbers are" ,even)

#To convert list into tuples:
a=[1,2,3]
b=tuple(a)
print(b)
# To convert tuple into list:
c=(3,6,9,12)
d=list(c)
print(d)
# To reverse the numbers
e=(9,18,27,36)
print(e[::-1])

#question

a=['black','red','yellow','orange','blue','pink']
b=[]
for i in a:
    if 'e' in i:
        b.append(i)
print(b)

#List comprehension
a=['black','red','yellow','orange','blue','pink']
b=[i for i in a if 'e' in i]
print(b)'''

#List comprehension
'''a=['black','red','yellow','orange','blue','pink']
b=[i for i in a if 'e' in i]
print(b)'''
#maximum number without using max() with range function
'''a=[1,2,3,4,5,6,7,8,9,10]
b=0
print(len(a))
for i in range(len(a)):
    for j in range(i+1):
        if a[j]>a[i]:
            b=a[j]
print(b)'''

# max number without range function
'''a=[9,7,9,19,11,23,28,21]
b=a[0]
for i in a:
    if i>b:
        b=i
print(b)'''

# min number without inbuilt and range function 
'''a=[9,7,9,19,11,23,28,21]
b=a[0]
for i in a:
    if i<b:
        b=i
print(b)'''