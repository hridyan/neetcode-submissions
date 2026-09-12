class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for idx in nums:
            if idx not in seen:
                seen.add(idx)
            else:
                return True
        return False