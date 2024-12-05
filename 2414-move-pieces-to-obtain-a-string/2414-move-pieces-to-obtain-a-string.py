class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s,t = 0, 0
        n = len(start)

        if Counter(start) != Counter(target):
            return False

        while s < n and t < n:
            while s < n and start[s] == '_':
                s += 1
            while t < n and target[t] == '_':
                t += 1
            
            if s < n and t < n:
                if start[s] != target[t]:
                    return False 
                if start[s] == 'L' and s < t:
                    return False
                if start[s] == 'R' and s > t:
                    return False

                s += 1
                t += 1
        
        return True
