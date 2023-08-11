# Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Key is a unique identifier, where we can find our data and value is that data.


# Creating and printing a dictionary.
UR5 = {'name': 'Uzair Rehman', 'age':20, 'goals':['Data Analyst', 'Machine Learning', 'Python', 'Problem Solving']}
print(UR5)

# Accessing the dictionary
print(UR5['name'])
print(UR5['goals'])
# print(UR5['contact'])           # This value doesn't exist, so this piece of code will give key error.

# Get method
print(UR5.get('name'))
print(UR5.get('contact'))              # This value doesn't exist, it'll give 'none' statement in return.
print(UR5.get('age', 'Not found'))     # If age(key) isn't in dictionary, then print 'Not found'.


# Adding new entry to dictionary
UR5['contact'] = '0304-2306890'
print(UR5)

# Updating value using update method in dictionary
UR5.update({'goals':['Data Analyst', 'Machine Learning', 'Python', 'Problem Solving', 'Developement']})
print(UR5)

# Deleting value in dictionary
del UR5['age']
print(UR5)

contact = UR5.pop('contact')        # This will return deleted value
print(contact)
print(UR5)

# To find how many keys are there in dictionary
print(len(UR5))

# To check all the keys of dictionary
print(UR5.keys())

# To check all the values of dictionary
print(UR5.values())

# To check both keys and values of dictionary
print(UR5.items())


for key, value in UR5.items():
    print(key, value)