***
Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10
***
n = int(input())
elements=[]
for _ in range(n):
    element = int(input())
    elements.append(element)
tuple_elements = tuple(elements)
print(min(tuple_elements))
