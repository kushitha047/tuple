***
 Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6
***
input_string = input()
tuple_elements = tuple(map(int, input_string.split()))
x = int(input())
count_x = tuple_elements.count(x)
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(count_x))
