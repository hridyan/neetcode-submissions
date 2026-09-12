class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        prefix=[1]*n
        postfix=[1]*(n)
        for i in range(1,n):
            prefix[i]=(prefix[i-1]*nums[i-1])
            postfix[n-i-1]=postfix[n-i]*nums[n-i]

        postfix[-1]=1
        for i in range(n):
            res[i]=prefix[i]*postfix[i]    
        return res