class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_s = []

        for k in s.lower():
            if k in 'abcdefghijklmnopqrstuvwxyz0123456789':
                stripped_s.append(k.lower())
        return stripped_s == stripped_s[::-1]