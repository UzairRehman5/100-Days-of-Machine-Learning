# "If", "Else" & "ELIF" in conditional statements.
language = 'Python'

if language == 'Java':
    print('Language is Java')

elif language == 'JavaScript':
    print('Language is JavaScript')

elif language == 'Python':
    print('Language is Python')

else:
    print('No match')



# "AND" & "OR" in condition statements.
skill_Python = True
skill_R = False
skill_Sql = True

if skill_Python and skill_Sql:          # In "AND" all conditions needs to be true.
    print("You're hired")

else:
    print("Sorry, you're not hired. Better luck next time!")


if skill_Python or skill_R:             # In "OR" only one condition needs to be true.
    print("You're hired")

else:
    print("Sorry, you're not hired. Better luck next time!")



# "NOT" in conditional statements.
logged_in = False

if not logged_in:
    print("Please log in")

else:
    print("Welcome")



# '==' vs object identity 'IS'

list_01 = [1, 2, 3]
list_02 = [1, 2, 3]

print(id(list_01))
print(id(list_02))

print(list_01 == list_02)
print(list_01 is list_02)           # The “is keyword” is used to test whether two variables belong to the same object. The test will return True if the two objects are the same else it will return False even if the two objects are 100% equal.

list_03 = list_01
print(id(list_01))
print(id(list_03))
print(list_01 is list_03)           # id(list_01) == id(list_03)

print(list_01 == list_03)



## False values
# False
# None
# Zero of any numeric type
# Any empty sequence. for example, '', (), [].
# Any empty mapping. for example, {}.

condition = 0

if condition:
    print("Evaluated to True")

else:
    print("Evaluated to False")

# Grade check project
percentage = int(input())

if percentage > 100:
    print("Percentage should be between 0-100")

elif percentage >= 80 and percentage < 100:
    print('Grade A+')

elif percentage >= 70 and percentage < 80:
    print('Grade A')

elif percentage >= 60 and percentage < 70:
    print("Grade B")

elif percentage >= 50 and percentage < 60:
    print("Grade C")

elif percentage >= 40 and percentage < 50:
    print("Grade D")

else:
    print('Fail')