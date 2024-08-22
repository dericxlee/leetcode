class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        counter = Counter(s1)
        left = 0
        curr_counter = Counter(s2[0:n])

        if n > len(s2):
            return False

        if curr_counter == counter:
            return True

        for right in range(n, len(s2)):
            curr_counter[s2[right]] = curr_counter.get(s2[right], 0) + 1
            curr_counter[s2[left]] -=1

            if curr_counter[s2[left]] == 0:
                del curr_counter[s2[left]]
            
            left+=1

            if curr_counter == counter:
                return True

        return False
