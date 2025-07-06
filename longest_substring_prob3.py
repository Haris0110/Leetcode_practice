class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0
        for right in range(len(s)) :
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len,right-left +1)
        return max_len
s = Solution()
print(s.lengthOfLongestSubstring(["bbbb"]))
'''this funtion in the class add charcter in the set and if the character repeat "
"it pops out the first character from the list and adds the new character"
"e.g for ["bbbb"] it adds b first in the set then it run the while condition'''