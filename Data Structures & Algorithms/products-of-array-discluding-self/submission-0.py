class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        if cnt[0]==0:
            output = []
            prod=1
            for n in nums:
                prod*=n
            for i in range(len(nums)):
                output.append(int(prod/nums[i]))
            return output
        if cnt[0]>=2:
            return [0]*len(nums)
        if cnt[0]==1:
            output = []
            prod = 1
            for n in nums:
                if n != 0:
                    prod*=n
            for i in range(len(nums)):
                if nums[i] == 0:
                    output.append(prod)
                else:
                    output.append(0)
            return output
        
        
        