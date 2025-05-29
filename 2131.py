# Lose
# You are given an array of strings words. Each element of words consists of two lowercase English letters.

# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

# Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

# A palindrome is a string that reads the same forward and backward.
# Example 2:

# Input: words = ["ab","ty","yt","lc","cl","ab"]
# Output: 8
# Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
# Note that "lcyttycl" is another longest palindrome that can be created.
# Example 3:

# Input: words = ["cc","ll","xx"]
# Output: 2
# Explanation: One longest palindrome is "cc", of length 2.
# Note that "ll" is another longest palindrome that can be created, and so is "xx".

words=input("word :").split(" ")
count={}
for i in words:
    if(i in count):
        count[i]+=1
    else:
        count[i]=1

length=0
used_middle = False
print(count)

for i in count:
    rev=i[::-1]
    if(i==rev):
        pair_count=count[i]//2
        length+= pair_count *2 *2
        count[i]-=pair_count*2
        if not used_middle and count[i] > 0:
            length += len(i)
            used_middle = True
    elif(rev in count):
        pair_count=min(count[i],count[rev])
        length+=pair_count*2*2
        count[rev]-=pair_count
        count[i]-=pair_count
    print(length)



