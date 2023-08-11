# for loop

list01 = [1, 2, 3, 4, 5]

for numbers in list01:
    print(numbers)


# Break statement
list02 = ['A', 'E', 'I', 'X', 'O', 'U']

for vowels in list02:
    print(vowels)
    if vowels == 'X':
        print('Found!')
        break


# Continue statement
list03 = [2, 44, 6, 123, 5, 764]

for favNum in list03:
    print(favNum)
    if favNum == 5:
        print('Found')
        continue


# Nested Loop

list04 = [10, 20, 30, 40, 50]
list05 = ['a', 'e', 'i', 'o', 'u']

for num in list04:
    for vowel in list05:
        print(num, vowel)



# Range function
for i in range(10):
    print(i)


for i in range(1, 11):
    print(i)



# While loop ; while loop will just keep going until the certain condition is met.

w = 0

while w == 10:
    print(w)
    w += 1

    

# Infinite loop
# x = 0
# while True:
#     print(x)
#     x += 1