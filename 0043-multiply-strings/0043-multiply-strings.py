class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def toInteger(str):
            result = 0

            for char in str:
                result *= 10
                result += (ord(char) - 48)
            
            return result

        return str(toInteger(num1)*toInteger(num2))

    
    
    

        