'''PYTHON PROGRAMMING LANGUAGE'''

# TYPE() - USES

'''
a=10
b="Yuvashree"
print(type(a))
print(type(b))
'''

#ouput = <class 'int'>  <class 'str'>


#TYPE CASTING - IS CONVERTING ONE DATATYPE TO ANOTHER DATATYPE

''' 
a="10"
b="20"
print(a+b)   
'''

#o/p 1020  becos the values are in str so type must be changed by type casting

''' 
A=int("10")
B=int("20")
print(A+B)
'''

#O/P is 30 becos we implemented int() in it and chnged the type of data  


# TO GET INPUT FROM USER  

'''
a=int(input())
b=int(input())
print(a+b)        
'''

# O/P is 10 20  ans 30 


# EXERCISE 
# 1

'''
name=input("Enter your name")
age=int(input("Enter your age"))
print("My Name is :",name)
print("My Age is:",age)
'''

#O/P Enter your name yuvi
#Enter your age21
#My Name is :  yuvi
#My Age is: 21

# 2

'''
x=20
y=10
z=100
p=x*y*z
q=x+y+z
print(p)
print(q)
'''
#O/P
#20000
#130

#IF ELSE

#1 BOOLEAN USAGE

'''
if True:
    print("yes")
else:
    print("No")
'''

#O/P Yes  

#2  VARIABLE USAGE

'''
yuvi="success"
if yuvi=="success":
    print("Ok")
else:
    print("not Ok ")'''

#O/P Ok

#3 INPUT,INT & DIVISIBLE

'''
num=int(input("enter number:"))
if num%4==0:
    print("It is divisible by 4:",num)
else:
    print("Not divisible be 4:",num)
'''

#O/P : enter number: 20 
# It is divisible by 4 , 20

#4  INPUT 

'''
mark=int(input("enter the mark :"))
if mark>=35:
    print("Pass:",mark)
else:
    print("Fail:",mark)
'''
#O/P enter the mark: 20  
#Fail:20
#enter the mark:35
#Pass:35

#5 AND & DIVISIBLE

'''
num=int(input("Enter the number:"))
if num%3==0 and num%5==0:
    print("It is divisible by 3 & 5:",num)
else:
    print("It is not divisible by 3 & 5:",num)
'''

#O/P : Enter the number:15
#It is divisible by 3 & 5: 15
#Enter the number:13
#It is not divisible by 3 & 5: 13

#6 EVEN OR ODD NUMBER

'''
number=int(input("Number:"))
if number%2==0:
    print(number,":Is Even")
else:
    print(number,":Is Odd")
'''

#O/P Number:30
#30 :Is Even
#Number:11
#11 :Is Odd


#ELIF OR ELSE IF STATEMENTS

#1 SCORES

'''
score=int(input("Enter your mark:"))
if score<=35:
    print("Poor")
elif score>35 and score<70:
    print("Average")
elif score<=100:
    print("Good")
else:
    print("Invalid")
'''

#O/P Enter your mark:100
#Good

#2 OPERATIONS 

'''
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
operations=input("add/sub/mul/div:")
if operations=="add":
    print(a+b)
elif operations=="sub":
    print(a-b)
elif operations=="mul":
    print(a*b)
elif operations=="div":
    print(a/b)
else:
    print("Invalid operation:")
'''

#O/P Enter number 1:10
#Enter number 2:2
#add/sub/mul/div:div
#5.0

#3 LOAN 

'''
age=int(input("enter your age :"))
salary=int(input("enter your salary:"))
if salary>=20000 or age>=20:
    print("you are eligible for loan ")
    loan=int(input("enter your loan amt:"))
    if loan==50000:
        print("maximum loan amt is 50000")
    else:
        print("loan amt cannot be extended ")
else:
    print("you are not eligible")
'''

#O/P enter your age :21     
#enter your salary:200000
#you are eligible for loan
#enter your loan amt:50000
#maximum loan amt is 50000

#4 MARKS TOT AND AVG

'''
math=int(input("enter your mark:"))
sci=int(input("enter your mark:"))
soc=int(input("enter your mark:"))
tam=int(input("enter your mark:"))
eng=int(input("enter your mark:"))
total=(math+sci+soc+tam+eng)
average=(total/5)
print(total)
print(average)
if average>35:
    print("Good to go")
else:
    print("You require extra class")
'''
#O/P enter your mark:50
#enter your mark:50
#enter your mark:50
#enter your mark:50
#enter your mark:50
#250
#50.0
#Good to go


###END###