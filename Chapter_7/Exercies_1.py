# Define a function that take a numbers(n)
# return a dictionary containing cube of numbers from 1 to n

# Example
# cube_finder(3)
# {1:1, 2:8, 3:27}

#________________Solution_______________


def cube_finder(n):
    cubes = {}
    for i in range(1,n+1):
        cubes[i] = i**3
    return cubes

n = input(' Enter a number : ')
n1 = int(n)
print(cube_finder(n1))