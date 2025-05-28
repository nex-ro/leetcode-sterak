# You are given positive integers n and m.

# Define two integers as follows:

# num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
# num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
# Return the integer num1 - num2.

# Example 1:

# Input: n = 10, m = 3
# Output: 19
# Explanation: In the given example:
# - Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], num1 is the sum of those integers = 37.
# - Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is the sum of those integers = 18.
# We return 37 - 18 = 19 as the answer.

n =int(input("non divisble :" ))
m=int(input("dividible :"))
def main():
    result=0
    for x in range(n+1):
        print(x)
        if(x%m!=0):
            result+=x
        else:
            result-=x
    print(result)



main()

    