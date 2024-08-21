class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = list()
        S, P = len(s), len(p)

        if P > S:
            return []

        p_count = Counter(p)
        s_count = Counter(s[:P])

        if p_count == s_count:
            ans.append(0)

        for i in range(P, S):
            s_count[s[i]] +=1
            s_count[s[i-P]] -=1

            if p_count == s_count:
                ans.append(i - P + 1)

        return ans
