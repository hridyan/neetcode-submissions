class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen={}
        for n in nums:
            if n not in seen:
                seen[n]=1
            else:
                seen[n]+=1
        max=nums[0]
        for p in seen:
            if seen[p]>seen[max]:
                max=p
        return max