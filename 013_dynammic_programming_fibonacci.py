# DYNAMMIC PROGRAMMING:
# ----------------------
# Making algo efficient by storing intermediate result
# Works well when algo has lots of repitetive computation
# To solve:
# 1. Recursion
# 2. Store(Memoize)
# 3. Bottom-up


# Fibonacci numbers is a series of numbers that start with [1, 1]
# and are formed by added the previous two number.
# Eg. Fibonnaci of n = Fibonnaci of (n-1) + Fobinacci of (n-2)
# Here 3rd Fibonacci will be (2nd + 1st) = (1+1) = 2
# [1, 1, 2, 3, 5] etc.

# Lets implement simple recursion to solve fibonacci series
# For every number we are calculating the fibonacci of the previous two indices.
# fibonacci_recursion() is called 2^n times.
# Hence O(2^n)
# Its very inefficient.

def fibonacci_recursion(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

    return result

# Lets add a storage to save the fiboncci that are already caluclated.
# Here the fibonacci_dynammic() function is called maximum 2n times
# O(n)

def fibonacci_dynammic(n, calculated_fibonacci):
    if calculated_fibonacci[n-1]:
        return calculated_fibonacci[n-1]
    elif n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci_dynammic(n-1, calculated_fibonacci) + fibonacci_dynammic(n-2, calculated_fibonacci)
    calculated_fibonacci[n-1] = result
    return result

# Lets implement the same using bottom-up approach
# Forloop is travered only n times
# O(n)

def fibonacci_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    first = 1
    second = 1
    for _ in range(0, n-2):
        result = first + second
        first = second
        second =  result
    return result

def main():
    assert fibonacci_recursion(5) == 5
    assert fibonacci_recursion(6) == 8

    assert fibonacci_dynammic(5, [None]*(5)) == 5
    assert fibonacci_dynammic(6, [None]*(6)) == 8

    assert fibonacci_bottom_up(5) == 5
    assert fibonacci_bottom_up(6) == 8

if __name__ == '__main__':
    main()
