# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

class Solution:
    def reverseWords(self, s: str) -> str:
        list1 = s.split(" ")
        result = ""
        for word in list1:
            word = word[::-1]
            result += word + " "
        return result[:-1]
