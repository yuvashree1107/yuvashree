a={1,2,3,4,5,6,7}
b={5,6,7,8,9}

# ADD A VALUE 

'''
b.add(10)
print(b)
'''

# O/P : {5, 6, 7, 8, 9, 10}

# REMOVE A VALUE 

'''
b.remove(5)
print(b)
'''

# O/P: {6, 7, 8, 9}

# INTERSECTION - PRINTS ONLY COMMON VALUES EXCLUDES OTHER ALL  (set1.intersection(set2) or & is used)

'''
print(a.intersection(b))
'''

#OR
 
'''
print(a&b)
'''

# O/P: {5, 6, 7}

# UNION - INCLUDES THE COMMON ONLY ONCE AND INCLUDES OTHER ALL VALUES ALSO (set1.union(set2) or | is used)

'''
print(a|b)
'''

#OR 

'''
print(a.union(b))
'''

# O/P : {1, 2, 3, 4, 5, 6, 7, 8, 9}

# SET DIFFERENCE - EXCLUDES ALL COMMON AND PRINTS VALUE IN SET 1 (set1.difference(set2) or - is used)

'''
print(a-b)
'''

# OR

'''
print(a.difference(b))
'''

#O/P : {1, 2, 3, 4}

# SYMMETRIC DIFFERENCE - EXCLUDES ALL COMMON AND ONLY INCLUDES UNCOMMON VALUES FROM BOTH THE SETS (set1.symmetric_difference(set2) or  ^ is used)


'''
print(a.symmetric_difference(b))

'''

# OR

'''
print(a^b)
'''

# O/P: {1, 2, 3, 4, 8, 9}


# SUBSET - IT CHECKS COMMON VALUES OF OF SUBSET IS IN SUPERSET (set1.issubset(set2) or <= is used) RETURNS T OR F


'''
print(a.issubset(b))
'''

# OR 


'''
print(a<=b)
'''

# O/P : False



# SUPERSET - IT CHECKS COMMON VALUES OF OF SUPERSET IS IN SUBSET (set1.issuperset(set2) or >= is used) RETURNS T OR F


'''
print(a.issuperset(b))
'''

# OR 

'''
print(a>=b)
'''

# O/P : False

# DISJOINT - CHECKS WHETHER THE SETS HAVE ONLY UNCOMMON VALUES AND RETURNS TRUE IF UNCOMMON ORESLE FALSE (set1.isdisjoint(set2))


'''
print(a.isdisjoint(b))
'''

# O/P : False

# SET EQUALITY - CHECKS WHETHER THE SETS ARE EQUAL ( == is used)


'''
print(a==b)
'''

# O/P:False

# SET COPY - COPIES ONE SET TO ANOTHER (newset.copy(set1) is used )

'''
d=a.copy()
print(d)
'''

# O/P : {1, 2, 3, 4, 5, 6, 7}