# Printing a string
message = 'Hello World'                     
print(message)

# Multiple quotations in a string
message01 = 'Hello World "Uzair"'           
print(message01)

# Multiple quotations in a string
message02 = ' "Hello World can\'t" he said at the time of his death' 
print(message02)

# String on multiple lines
message03 = '''Goals:                      
1) Internship
2) Good paying job
3) Collect money for the Hajj'''
print(message03)



compliment = '"Excellent", she said'

# Printing length
print(len(compliment))

# Printing specific part of a string
print(compliment[1:10])
print(compliment[13:21:2])
print(compliment[13:])

# Uppercasing the string
print(compliment.upper())

# Counting how many times the mentioned text has repeated in a string
print(compliment.count('x'))
print(compliment.count('she'))


# Finding if the mentioned text is in string or not
print(compliment.find('s'))
print(compliment.find('eat'))

# Relacing word within a string
print(compliment.replace('she', 'he'))



name = 'Uzair Rehman'
job_title = 'Data Scientist'
age = 'Male'

# String concordenation
UR5 = name + '\n ' + job_title
print(UR5)

# String formatting
bio = '{} \n {} \n {}' .format(name, job_title, age)
print(bio)

# F-string
self = f'\n{name}\n{job_title}\n{age}. \nEND'
print(self)



# 'dir' function
print(dir(self))

# 'help' function
print(help(str))
print(help(str.lower))