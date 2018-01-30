'''
Multiples of 3 and 5
--------------------
Question taken from: https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below given user input integer.
'''


def sum_up_3_or_5_multiples(upper_range):
    sum = 0
    for number in range(upper_range):
	if number % 3 == 0 or number % 5 == 0:
	    sum += number
    return sum

def main():
    upper_range = int(input("Please enter a number to find sum of all multiples of 3/5 below that."))
    sum = sum_up_3_or_5_multiples(upper_range)
	print("Sum of all the multiples of 3/5 below ", upper_range, " is: ", sum)

if __name__ == "__main__":
    main()
