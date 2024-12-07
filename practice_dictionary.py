a={'name':'yuvi','age':21,'degree':'BCA',  'salary': 200000, 'Role': 'PFS Developer', 'company': 'Accenture','course': 'PFS', 'Area': 'Tambaram'}

# TO ADD A NEW ITEM 

'''a['course']='PFS'
a['Area']='Tambaram'
print(a)
'''
# O/P : {'name': 'yuvi', 'age': 21, 'degree': 'BCA', 'course': 'PFS', 'Area': 'Tambaram'}

# TO UPDATE MULTIPLE VALUES
 
'''
b={'salary':200000,'Role':'PFS Developer','company':'Accenture'}
a.update(b)
print(a)
'''
# O/P : {'name': 'yuvi', 'age': 21, 'degree': 'BCA', 'salary': 200000, 'Role': 'PFS Developer', 'company': 'Accenture'}

# DELETE - USING KEYWORD 

'''del a['Area']
print(a)
'''

# O/P:{'name': 'yuvi', 'age': 21, 'degree': 'BCA', 'salary': 200000, 'Role': 'PFS Developer', 'company': 'Accenture', 'course': 'PFS'}

# DELETE - USING POPITEM() WITHOUT ID 

'''
a.popitem()
print(a)
'''

# O/P: {'name': 'yuvi', 'age': 21, 'degree': 'BCA', 'salary': 200000, 'Role': 'PFS Developer', 'company': 'Accenture', 'course': 'PFS'}

# DELETE - USING POP() USING ID 

'''
a.pop('Role')
print(a)
'''

# O/P: {'name': 'yuvi', 'age': 21, 'degree': 'BCA', 'salary': 200000, 'company': 'Accenture', 'course': 'PFS', 'Area': 'Tambaram'}

#  CLEAR()

'''
b={'abc':'abcd','hgn':21}
b.clear()
print(b)
'''

# O/P : {}

# PRINT STATEMENTS - DICT FUNCTIONATILIES


print(a.keys())

# O/P: dict_keys(['name', 'age', 'degree', 'salary', 'Role', 'company', 'course', 'Area'])


print(a.values())

# O/P : dict_values(['yuvi', 21, 'BCA', 200000, 'PFS Developer', 'Accenture', 'PFS', 'Tambaram'])


print(a.items())

# O/P : dict_items([('name', 'yuvi'), ('age', 21), ('degree', 'BCA'), ('salary', 200000), ('Role', 'PFS Developer'), ('company', 'Accenture'), ('course', 'PFS'), ('Area', 'Tambaram')])


