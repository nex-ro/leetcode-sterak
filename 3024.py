# You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.

# A triangle is called equilateral if it has all sides of equal length.
# A triangle is called isosceles if it has exactly two sides of equal length.
# A triangle is called scalene if all its sides are of different lengths.
# Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

# Example 1:

# Input: nums = [3,3,3]
# Output: "equilateral"
# Explanation: Since all the sides are of equal length, therefore, it will form an equilateral triangle.

number=input("array of number divide by space :").split(" ")
def triangleType( nums):
    if(nums[0]==nums[1] and nums[1]==nums[2]):
        return("equilateral")
    elif(
        (nums[0]==nums[1] and nums[0]+nums[1]>nums[2]) or 
        (nums[0]==nums[2] and nums[0]+nums[2]>nums[1])or 
        (nums[2]==nums[1] and nums[2]+nums[1]>nums[0])
    ):
        return("isosceles")
    elif(nums[0] + nums[1] >nums[2] and nums[0] + nums[2] >nums[1] and nums[1] + nums[2] >nums[0]):
        return("scalene")
    else:
        return("none")
    
print(triangleType(number))