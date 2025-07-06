class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)) : 
            for j in range(len(nums)):
                if i != j:
                    sum = nums[i]+nums[j]
                    if sum == target:
                        return i,j
                    
sol = Solution()
print(sol.twoSum([1, 3, 2, 5, 7],12))  