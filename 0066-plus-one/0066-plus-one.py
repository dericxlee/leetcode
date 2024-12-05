class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            sum = digits[i] + carry

            carry = sum // 10
            digit = sum % 10

            digits[i] = digit
        
        return digits if not carry else [carry] + digits