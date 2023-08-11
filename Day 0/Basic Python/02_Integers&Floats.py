# Printing type of number
num01 = 3.142
print(type(num01))


##  Arithmetic Operator

# Addition : 3 + 2
# Subtraction : 3 - 2
# Multiplication : 3 * 2
# Division : 3 / 2           (Division always return in float)
# Floor Division : 3 // 2    (Floor division always return in integer)
# Exponent : 3 ** 2
# Modulus : 3 % 2            (Remainder) & it's commonly used in checking whether the no is even or odd.


num02 = 5

# Incrementing the number
num02 = num02 + 1
print(num02)

num02 += 1
print(num02)

# Multiplying the number
num02 *= 10
print(num02)


# Absolute value of a number
num03 = -8
print(abs(num03))


# Rounding of a number
num04 = 3.142
print(round(num04))
print(round(num04, 2))


## Comparison

# Equal : 3 == 2
# Not Equal : 3 !=  2
# Greater than : 3 > 2
# Less than : 3 < 2
# Greater or Equal : 3 >= 2
# Lesser or Equal : 3 <= 2


# Type Casting
num05 = '100'
num06 = '200'
num = int(num05) + int(num06)
print(num)