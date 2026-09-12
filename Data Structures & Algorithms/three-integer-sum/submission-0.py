class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            target = -1*nums[i]
            a=self.twoSum(nums[i+1:], target)
            b=[[nums[i]]+item for item in a]
            res.extend(sorted(b))
        return [list(x) for x in set(tuple(x) for x in res)]

    
    def twoSum(self, nums,target):
        seen = set()
        res=[]
        for i in sorted(nums):
            complement = target - i
            if complement in seen:
                res.append([i,complement])
            else:
                seen.add(i)
        return res