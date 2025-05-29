# Given a string s of zeros and ones, return the maximum score after 
# splitting the string into two non-empty substrings (i.e. left substring and right substring).
# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
# Example 1:
# Input: s = "011101"
# Output: 5 
# Explanation: 
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3
# Example 2:

# Input: s = "00111"
# Output: 5
# Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

s=input("number:")
rev=s[::-1]
result=[]

for i in range(len(s)-1) :
    tempkiri=0
    tempkanan=0
    kiri=s[0:(i+1)]
    for j in kiri :
        if(j=="0"):
            tempkiri+=1

    kanan=s[-(len(s)-1-i):]
    for j in kanan :
        if(j=="1"):
            tempkanan+=1
    result.append((tempkanan+tempkiri))


print(max(result))

# best possbility
# def maxScore(self, s):
#        left_zeros = 0
#        right_ones = s.count('1')
#        max_score = 0
#        for i in range(len(s) - 1):  # 不能切在最後一個
#            if s[i] == '0':
#                left_zeros += 1
#            else:
#                right_ones -= 1
#            max_score = max(max_score, left_zeros + right_ones)
#        return max_score

    
        
        


