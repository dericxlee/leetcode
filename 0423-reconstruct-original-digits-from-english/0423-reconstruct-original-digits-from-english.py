class Solution:
    def originalDigits(self, s: str) -> str:
        digits = [0]*10
        freq = Counter(s)

        digits[0] = freq["z"]
        digits[2] = freq["w"]
        digits[4] = freq["u"]
        digits[6] = freq["x"]
        digits[8] = freq["g"]
        digits[1] = freq["o"] - digits[4] - digits[2] - digits[0]
        digits[5] = freq["f"] - digits[4]
        digits[7] = freq["v"] - digits[5]
        digits[3] = freq["h"] - digits[8]
        digits[9] = freq["i"] - digits[8] - digits[5] - digits[6]

        res = ""

        for i, digit in enumerate(digits):
            res += str(i)*digit
        
        return res
            


        


