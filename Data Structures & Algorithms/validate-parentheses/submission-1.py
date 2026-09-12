class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        count=0
        dictionary = {'{':'}','[':']','(':')'}
        for c in s:
            if c in '{[(':
                stack.append(c)
                count+=1
            elif c in '}])':
                if stack and dictionary.get(stack[-1])==c:
                    count-=1
                    stack.pop(-1)
                else:
                    return False
        if count==0:
            return True
        return False
