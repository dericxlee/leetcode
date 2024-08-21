class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        lookup = dict()
        ans = list()

        for i in range(9, len(s)):
            seq = s[i-9: i+1]
            if seq in lookup and lookup[seq] == 1:
                ans.append(seq)
                lookup[seq] +=1
            elif seq not in lookup:
                lookup[seq] = 1
            else:
                lookup[seq] +=1


        return ans