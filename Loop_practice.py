# FOR LOOP

#1 APPLE

'''
for i in "apple":
    print(i)
'''

# O/P a
#p
#p
#l
#e

# 2 RANGE 

'''
for i in range(5):
    print(i)
'''

#O/P 0
#1
#2
#3
#4

# 3 RANGE WITH START AND END VALUE

'''
for i in range(1,4):
    print(i)
'''

#O/P 1
#2
#3

# 4 TABLES

'''
for i in range(1,11):
    print(i,"*4=",i*4)
'''

#O/P 1 *4= 4
#2 *4= 8
#3 *4= 12
#4 *4= 16
#5 *4= 20
#6 *4= 24
#7 *4= 28
#8 *4= 32
#9 *4= 36
#10 *4= 40

#5 NUM B/W 8-15

'''
a=int(input())
b=int(input())
for i in range(a+1,b):
    print(i)
'''

# O/P 8
#16
#9
#10
#11
#12
#13
#14


#6 EVEN NUM B/W 1-10

'''
for i in range(1,11):
    if i%2==0:
        print(i)
'''

#O/P 2
#4
#6
#8
#10


#7 COUNT OD ODD NUM B/W 1-10

'''
countodd=0
for i in range(1,11):
    if i%2!=0:
        countodd=countodd+1
print(countodd)
'''

#O/P 5

#8  COUNT BOTH ODD AND EVEN NUM B/W 1-10

'''
countodd=0
counteven=0
for i in range(1,11):
    if i%2==0:
        counteven=counteven+1
    else:
        countodd=countodd+1
print(counteven)
print(countodd)
'''

#O/P 5
#5

#9 COUNT NUM DIVISIBLE BY 3 & 5

'''
count=0
for i in range(1,101):
    if i%3==0 and i%5==0:
        count=count+1
print(count) 
'''

#O/P 6

#10 SUM OF FIRST 5 NATURAL NUMBERS

'''
sum=0
for i in range (1,6):
    sum=sum+i
print(sum)
'''

#O/P 15

#11 SUM OF 5 NUMB FROM KEYBOARD

'''
a=[]
print("Enter 5 numbers:")
for i in range(5):
    num=int(input("enter num"+str(i)))
    a.append(num)
print(a)
sum=0
for i in a:
    sum=sum+i
print(sum)
'''

#O/P Enter 5 numbers:
#enter num010
#enter num120
#enter num230
#enter num340
#enter num450
#[10, 20, 30, 40, 50]
#150


#12 SUM OF 7 NATURAL NUM

'''
sum=0
for i in range(1,8):
    sum=sum+i
print(sum)
'''

#O/P 28

#13 CUBE OF 5 NUMBERS

'''
for i in range(1,6):
    print("Number is:",i,"and cube of",i,"is:",i*i*i)
'''

#O/P 
#Number is: 1 and cube of 1 is: 1
#Number is: 2 and cube of 2 is: 8
#Number is: 3 and cube of 3 is: 27
#Number is: 4 and cube of 4 is: 64
#Number is: 5 and cube of 5 is: 125

#NESTED LOOP

#14 SAMPLE

'''
for i in range(1,6):
    for j in range(1,3):
        print(j,"Apple")
'''

#O/P 1 Apple
#2 Apple
#1 Apple
#2 Apple
#1 Apple
#2 Apple
#1 Apple
#2 Apple
#1 Apple
#2 Apple


#15 PATTERN 

'''
for i in range(1,6):
    print()
    for j in range(1,i+1):
        print("* ",end=" ")
print()  
'''

#O/P * 
#    *  * 
#    *  *  * 
#    *  *  *  * 
#    *  *  *  *  *



# WHILE LOOP

# 16 PRINT 5 NUMBERS

'''
i=1
while i<=5:
    print(i,end=",")
    i=i+1
'''

#O/P  1,2,3,4,5

# 17 PRINT 10,20,30-200

'''
i=10
while i<=200:
    print(i,end=",")
    i=i+10
'''

#O/P 10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200


# 18 REVERSE 10 NUMBERS

'''
i=10
while i>0:
    print(i,end=",")
    i=i-1
'''

# O/P 10,9,8,7,6,5,4,3,2,1


# 19 FACTORIAL

'''
i=3
factorial=1
while i>0:
    factorial=factorial*i
    i=i-1
print(factorial)
'''

#O/P 6

