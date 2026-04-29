class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()

                if token == "+":
                    sub = first + second
                elif token == "-":
                    sub = first - second
                elif token == "*":
                    sub = first * second
                elif token == "/":
                    sub = abs(first) // abs(second)
                    if (first < 0 or second < 0) and not (first < 0 and second < 0):
                        sub *= (-1)

                stack.append(sub)
        
        return stack[-1]
                