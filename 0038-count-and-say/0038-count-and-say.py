class Solution:
    def countAndSay(self, n: int) -> str:
        iteration = 1
        string = "1"

        while iteration < n:
            freq = 0
            num = ""
            new_string = ""

            for char in string:
                if char == num:
                    freq += 1
                else:
                    if freq:
                        new_string += str(freq) + num

                    freq = 1
                    num = char
            
            string = new_string + str(freq) + num
            iteration += 1
        
        return string
