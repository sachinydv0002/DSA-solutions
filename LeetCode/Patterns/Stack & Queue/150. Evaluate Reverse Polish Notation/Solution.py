class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            
            else:
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    result = a + b
                elif t == "-":
                    result = a - b
                elif t == "*":
                    result = a * b
                else: 
                    result = abs(a) // abs(b)
                    i

                stack.append(result)
        
        return stack[-1]