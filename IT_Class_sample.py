'''a = 20
b = 30
c = a + b
print("The sum of", a, "and", b, "is", c)'''

'''a=int(input("ENTER VALUE A :"))
b=int(input("ENTER VALUE B:"))
c=a+b
print(c)'''

'''a=90
b=70
c=a+b
print("the sum of {} and {} is {}.".format(a,b,c))'''

a=int(input("Enter the value pi"))
b=int(input("enter the value r"))
# find the area of circle 
# Area of circle = pi*r*r --pi= 22/7 or 3.14
'''r=int(input("Enter the r value"))
pi=3.14
area= pi*r*r
print("The area of circle is ",int(area))  '''

# find area of rectangle
# area of rectangle = l*b
'''l=int(input("enter the l value"))
b=int(input("enter the b value"))
area= l*b
print("the area of rectangle is", area)'''

#check whether he/she is eligible for vote casting
''' syntax:
    if condition:
         true statement
    else:
         false statement '''
     
     #code

'''a=int(input("enter the age"))
if a>17:
    print("he/she is eligible for vote casting")
else: 
    print("he/she is not eligible for vote casting")'''

# to check whether the password is correct or not
#code

'''pwd=input("enter the password")
if pwd =="l@p123":
    print("home page")
else:
    print("retry")'''

                                 # Nested if

# check whether the given gmail and pwd is valid or invalid using nested if

'''gmail="lavs@gmail.com"
pwd="123"
if gmail=="lavs@gmail.com":
    if pwd=="123":
        print("homepage")
    else:
        print("invalid pwd")
else:
    print("invalid gmail")'''

#compare 3 numbers and say which is greater (elif)


'''a=30          
b=20
c=5
if a>b and a>c:  # and is a logical operator using else if
    print("a is big")
elif b>c:
    print("b is big")
else:
    print("c is big") '''

                                       #while loop
'''a=1
while a<=5:
    a=a+1
    print (a)'''

# check whether the password for 5 times after 5 times print wait for 30 seconds

'''a=1
while a<=5:
    pwd=input("enter the password")
    if pwd=="lavs@123":
        print("home page")
        break
    else:
        print("retry")
    a=a+1
else:
    print("wait for 30 seconds")'''

# write a python code to check whether the given number is even or odd.

'''a=int(input("enter the value"))
if a%2==0:
    print("even")

else:
    print("odd") '''

# write a python code to check whether the given number is odd or even without using modulas symbol.

'''a=int(input("enter the value"))
if (a//2)*2==a:
    print("even")
else:
    print("odd")'''

'''case 1
    a=12
    (12//2)*2==12
    6*2==12
    12==12

case 2
    a=3
    (3//2)*2==3
    1*2==3
    2==3'''

    # For loop
#for i in range(6):
# print(i)'''

'''a="python"
for j in a:
    print(j)'''
# write code for the below output

# *
# * *
# * * *
# * * * *
# * * * * * 

'''for row in range(6):
    for col in range(row+1): 
        print("* ",end="")
    print()   '''

# 1 2 3 4 5 
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25

'''for row in range(1,6):
    for col in range(1,6):
        print(row*col, end="")
    print()'''

'''# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(5, 0, -1):
    print('*' * i)


# * * * * *
#   * * * *
#     * * *
#       * *
#         *
row=5
for i in range(row,0,-1):
    for j in range(row-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()'''

'''      *
      *     *
   *     *    *  
 *     *    *    * 
*    *   *   *     *   '''

'''n = 5  
for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    for j in range(1, i + 1):
        print('*', end=' ')
    print()'''

#a=[9,7,8,10,8]
#a.pop()
#print(a)

#a.pop(1)
#print(a)

#del a
#print(a)

'''a=[1,2,3,4,5]
sum=0
for i in a:
    sum=sum+i
print("sum:",sum)'''

'''product=1
for i in a:
    product=product*i
print("product: ",product)'''

