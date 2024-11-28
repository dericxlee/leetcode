class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }

        for token in tokens:
            if token in operators:
                y = stack.pop()
                x = stack.pop()

                num = int(operators[token](x, y))
                stack.append(num)
            else:
                stack.append(int(token))
        
        return stack[-1]


