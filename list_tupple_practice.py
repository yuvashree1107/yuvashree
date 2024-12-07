# LIST 


'''a=[1,2,3,4,5,6,7,[8,9,10],11,12,13]
b=[14,15,1,2,3,15,15,16,17]  
'''  

#INDEXING 

'''print(a[1])
print(a[7])'''

# O/P: 2
# [8,9,10]


#NESTED INDEXING 

'''print(a[7][2])'''

# O/P : 10

#CONACT

'''print(a+b)'''

# O/P : [1, 2, 3, 4, 5, 6, 7, [8, 9, 10], 11, 12, 13, 14, 15, 1, 2, 3, 15, 15, 16, 17]


#SLICING 

'''print(a[2:8])
print(a[2:])
print(a[:6])'''


# O/P :[3, 4, 5, 6, 7, [8, 9, 10]]
#      [3, 4, 5, 6, 7, [8, 9, 10], 11, 12, 13]
#      [1, 2, 3, 4, 5, 6]


# DOUBLE SLICING 

'''print(a[1:8:2])
print(a[::-1])  ''' #reverse slice


# O/P : [2, 4, 6, [8, 9, 10]]
#       [13, 12, 11, [8, 9, 10], 7, 6, 5, 4, 3, 2, 1]


# METHODS 

# APPEND()

'''b.append(20)
print(b)'''

# O/P : [14, 15, 1, 2, 3, 15, 15, 16, 17, 20]

# EXTEND()

'''a.extend(b)
print(a)
'''
# O/P :[1, 2, 3, 4, 5, 6, 7, [8, 9, 10], 11, 12, 13, 14, 15, 1, 2, 3, 15, 15, 16, 17]

# INSERT()

'''a.insert(3,100)
print(a)'''

# O/P :[1, 2, 3, 100, 4, 5, 6, 7, [8, 9, 10], 11, 12, 13]

# POP()
 
'''a.pop()       #WITHOUT POSITION
a.pop(3)      #WITH POSITION 
print(a)
'''
# O/P : [1, 2, 3, 5, 6, 7, [8, 9, 10], 11, 12]

# REMOVE()

'''
a.remove(3)   # WITH SPECIFIED VALUE TO BE DELETED
print(a)
'''

# O/P:[1, 2, 4, 5, 6, 7, [8, 9, 10], 11, 12, 13]

# CLEAR()

'''a.clear()
print(a)
'''

# O/P: []

# FUNCTIONALITIES OF LIST 

# MAX(),MIN(),LEN(),SUM()

############################################  END OF LIST OPERATIONS ############################################### 


# TUPLES 

'''
a=(1,2,3,4,5,6)
b=(7,8,9,10,11,12)
'''

# REVERSE SLICING 

'''print(a[::-1])'''

# O/P:(6, 5, 4, 3, 2, 1)

# SLICING

'''print(a[:4])'''

# O/P: (1, 2, 3, 4)
     
# TUPLE TO LIST CONVERSION  

'''
c=list(b)
print(c)
'''

# O/P: [7, 8, 9, 10, 11, 12]

# LIST TO TUPLE CONVERSION

'''
c=[1,2,3]
d=tuple(c)
print(d)
'''

# O/P: (1, 2, 3)


#################################################### END OF TUPLES ################################################################