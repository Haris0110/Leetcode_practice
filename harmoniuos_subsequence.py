from collections import Counter
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        c = Counter(nums)#Counter is from collections
        output = 0
        for k,v in c.items():
            if k+1 in c:
                output = max(output,v+c[k+1])
        return output

    'this program calculates the largest harmonious subsequence means it calculates the length '
    'of a list between the numbers which have high frequency on a condition that the maximum value '
    'and the minimum value of the list should be differ by 1' 

sol = Solution()
sol.findLHS([1, 3, 2, 2, 5, 2, 3, 7])# we can change the list

            
        