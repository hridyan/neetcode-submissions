
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def translate(a,b,op)->int:
            match op:
                case '+':
                    return a+b
                case '-':
                    return a-b
                case '*':
                    return a*b
                case '/':
                    return int(a/b)
            return 0
        stack=[]
        for t in tokens:
            if t not in '+-/*':
                stack.append(int(t))
            else:
                b=stack.pop()
                a=stack.pop()

                n = stack.append(translate(a,b,t))
        return stack[0]