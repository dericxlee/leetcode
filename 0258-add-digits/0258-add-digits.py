class Solution:
    def addDigits(self, num: int) -> int:
        string = str(num)

        while len(string) > 1:
            total = 0
            for s in string:
                total += int(s)
            
            string = str(total)
        
        return int(string)