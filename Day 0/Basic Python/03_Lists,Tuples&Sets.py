# List is a class of data structures that can store one or more objects or values. A list is used to store multiple items in one variable and can be created using square brackets. 

# Creating & Printing a list
myFavPlayers = ['Messi', 'Griezmann', 'Pedri', 'Araujo', 'Enzo']
print(myFavPlayers)

# Printing length of list
print(len(myFavPlayers))

# Indexing list
print(myFavPlayers[2])
print(myFavPlayers[-1])
print(myFavPlayers[2:5])
print(myFavPlayers[1:])

## Modifying lists

# Adding element at the last of list
myFavPlayers.append('Isco')
print(myFavPlayers)

# Adding element at any position of a list
myFavPlayers.insert(1, 'Puyol')
print(myFavPlayers)

 
# Adding element of a list in another list
subjects = ['Software Engineering', 'Computer Science', 'Data Structure', 'Business Economics']
subjects_math = ['Linear Algebra', 'Calculus', 'Differential Equation']

subjects.extend(subjects_math)
print(subjects)
print(len(subjects))

# Adding list in a list
fields = ['Civil Engineering', 'Mechanical Engineer', 'Electrical Engineer']
fields_Computer = ['Software Engineering', 'System Engineering', 'Computer Scientist']
fields_Arts = ['Designing', 'Sketching']

fields.insert(0, fields_Computer)       # Inserting list at zeroth index of list
print(fields)

fields.append(fields_Arts)                   # Inserting list at the last index of list
print(fields)

print(len(fields))
print(fields[0])
print(fields[0:3])


# Removing elements of a list
fav_Num = ['5', '10', '3', '56', '25']
fav_Num.remove('56')
fav_Num.pop()                                 # Will remove element from the last index of list
print(fav_Num)


# Reversing a list
fav_Num.reverse()
print(fav_Num)


# Sorting a list
colors = ['Red', 'Orange', 'Green', 'Black', 'Blue']
colors.sort()
print(colors)


# Finding index of element in a list
print(colors.index('Black'))


# Finding if the value exists in list or not
print('Blue' in colors)
print('Brown' in colors)


# Sorting the list in a increasing way
num = [7,3,71,12,34,53,11,10]
num.sort()
print(num)


# Sorting the list in a decreasing way
num.sort(reverse=True)
print(num)


# Printing smallest number of the list
print(min(num))


# Printing the largest number of list
print(max(num))


# Printing sum of all the numbers in list
print(sum(num))

# 'Sorted' function is useful when you don't want to alter the original list, sorted function doesn't work on original list, you must have to create a copy of original file.
marks = [78,79,87,69,70,70]
marks_copy = sorted(marks)
print(marks_copy)


# Printing the list through loop
countries = ['Qatar', 'Kuwait', 'Saudi Arabia', 'UAE', 'Canada']

for country in countries:
    print(country)


# Printing the list through loop with index number
for index, country in enumerate(countries):
    print(index, country)


# Printing the list through loop with index number starting with 1
for index, country in enumerate(countries, start = 1):
    print(index, country)


# Converting list into string
cities = ['Islamabad', 'Multan', 'Moro']
cities_str = ', '.join(cities)
print(cities_str)

# Converting string into list
cities_list = cities_str.split(', ')
print(cities_list)




# Tuples are same as list, but we can't modify tuples. Tuples are immutable. But we can loop through the tuple and can access the tuple.

# Creating and printing a tuple
tuple_1 = ('A', 'E', 'I', 'O', 'U')
print(tuple_1)

# Trying to modify tuple, but it's not possible.
# tuple_1[0] = 'X'
# print(tuple_1)





# Sets are values that are unordered and also have no duplicates values.

#  Creating and printing a sets
continents = {'Asia', 'Africa', 'Europe', 'Oceania', 'Antartica'}
print(continents)

# Duplicate test
continents = {'Asia', 'Africa', 'Europe', 'Oceania', 'Antartica', 'Europe', 'North America', 'South America'}
print(continents)

# Membership test (we can do this with lists and tuples also, but sets are optimized for this)
print('Antartica' in continents)
print('Artric' in continents)


Messi = {'Goals', 'Assists', 'Playmaking', 'Dribbling', 'Freekicks'}
Ronaldo = {'Goals', 'Assists', 'Penalty', 'Physical'}

# Intersection (Common elements in both set)
print(Messi.intersection(Ronaldo))

# Difference (Element of first set - Element of second set)
print(Messi.difference(Ronaldo))

# Union (All elements of all sets)
print(Messi.union(Ronaldo))




# Empty lists
Empty_list01 = []
print(Empty_list01)

Empty_list02 = list()
print(Empty_list02)


# Empty tuples
Empty_tuples01 = ()
print(Empty_tuples01)

Empty_tuples02 = tuple()
print(Empty_tuples02)


# Empty sets
Empty_set01 = {}                # This isn't a empty set. It's a dictionary
print(Empty_set01)

Empty_set02 = set()
print(Empty_set02)
