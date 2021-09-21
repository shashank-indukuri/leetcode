# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = []
        queueDict = {}
        maxLen = 0
        
        for char in s:
            while char in queueDict:
                k = queue.pop(0)
                queueDict.pop(k)
            queue.append(char)
            queueDict[char] = char
            queueLen = len(queue)
            maxLen = max(maxLen, queueLen)
                
        return maxLen
