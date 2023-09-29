# Creating an array
from array import array
arr = array("i", [1,2,3,4,5])
print("The elements of array are: ", end=" ")
for i in range(0, 5):
    print(arr[i], end=" ")
print('\r')


# Array consisting of float
arr_float = array("d", [1.4032,2.64,3.22,4.52,5.31])
print("The elements of array are: ", end=" ")
for i in range(0, 5):
    print(arr_float[i], end=" ")
print('\r')


# Array consisting of large integers
arr_int = array("q", [14032,264,322,452,5293229391])
print("The elements of array are: ", end=" ")
for i in range(0, 5):
    print(arr_int[i], end=" ")
print('\r')


# printing type
print("Type :", type(arr))       


# Python append() Method
# using append() to insert new value at end
arr.append(6)
print("The appended array : ", end=" ")
for i in range(0,6):
    print(arr[i], end=" ")
print('\r')


# Array insert(i,x) Method in Python
arr.insert(0,0)
print('The array after insertion : ', end=" ")
for i in range(0,7):
    print(arr[i], end=" ")
print("\r")


# array pop() Method in Python
# using pop() to remove element at 2nd position
arr.pop(5)
print('The array after popping is : ', end=" ")
for i in range(0,6):
    print(arr[i], end=" ")
print("\r")


# Array remove() in Python
# using remove() to remove 1st occurrence of 4
arr.remove(4)
print("The array after removing element : ", end="")
for i in range(0,5):
    print(arr[i], end=" ")
print('\r')


# Array index() Method
# using index() to print index of 1st occurrence of 2
print('The index of 1st occurrence of 6 is :', arr.index(6))
# print('\r')


# Array reverse() Function
#using reverse() to reverse the array
arr.reverse()
print('The array after reversing is : ', end="")
for i in range(0,5):
    print(arr[i], end="")
print('\r')