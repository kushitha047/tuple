***
Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60
***
input_string = input()
tuple_elements = tuple(map(int, input_string.split()))
total = 0
for element in tuple_elements:
    total += element
print(total)
