***
 Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30
***
n = int(input())
elements = []
for _ in range(n):
    element = int(input())
    elements.append(element)
tuple_elements = tuple(elements)
print(max(tuple_elements))
