class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen_nums = {}
        res= []
        for n in nums:
            if n not in seen_nums:
                seen_nums[n] = 1
            else:
                seen_nums[n] = seen_nums[n] + 1
        
        sorted_data = {k:v for k,v in sorted(seen_nums.items(), key = lambda item:item[1], reverse=True)}

        ls = list(sorted_data.keys())
        return ls[:k]