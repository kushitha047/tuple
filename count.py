***
 Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
Sample Input:
10 20 30
Sample Output:
3
***
input_string = input()
tuple_elements = tuple(map(int, input_string.split()))
print(len(tuple_elements))
