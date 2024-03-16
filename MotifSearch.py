# Python3 program for the above approach
from collections import deque, Counter, defaultdict
import sys

# Function that generates substring
# of length K that occurs maximum times
def maximumOccurringString(s, K):

   # Store the frequency of substrings
   M = {}

   # Deque to maintain substrings
   # window size K
   D = deque()

   for i in range(K):
      D.append(s[i])

   # Update the frequency of the
   # first substring in the Map
   # E="".join(list(D
   M[str("".join(list(D)))] = M.get(
      str("".join(list(D))), 0) + 1

   # Remove the first character of
   # the previous K length substring
   D.popleft()

   # Traverse the string
   for j in range(i, len(s)):

      # Insert the current character
      # as last character of
      # current substring
      D.append(s[j])

      M[str("".join(list(D)))] = M.get(
         str("".join(list(D))), 0) + 1

      # Pop the first character of
      # previous K length substring
      D.popleft()

   maxi = -sys.maxsize - 1

   ans = deque()

   # Find the substring that occurs
   # maximum number of times
   # print(M)
   for it in M:
      
      # print(it[0])
      if (M[it] >= maxi):
         maxi = M[it]
         
         # print(maxi)
         ans = it

   # Print the substring
   res = ""
   for i in range(len(ans)):
      res += ans[i]
      #print(ans[i], end = "")
   return res

# Driver Code
if __name__ == '__main__':
	
	# Given string
	s = "TTTTT"

	# Given K size of substring
	K = 5

	# Function call
	print(maximumOccurringString(s, K))

# This code is contributed by mohit kumar 29
