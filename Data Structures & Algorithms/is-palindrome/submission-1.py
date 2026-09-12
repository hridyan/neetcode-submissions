class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        non_alnum = "".join(c for c in set(s) if not c.isalnum())
        stripped_s = s.translate(str.maketrans("", "", non_alnum))
        print(stripped_s)
        i=0
        j=len(stripped_s)-1
        while i<=j:
            if stripped_s[i]==stripped_s[j]:
                i+=1
                j-=1
            else:
                return False
        return True