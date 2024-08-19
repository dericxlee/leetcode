class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        ans = 0
        _count = 0

        for i in moves:
            if i == "L":
                ans -= 1
            elif i == "R":
                ans += 1
            else:
                _count += 1
        
        if ans > 0:
            return ans + _count
        else:
            return abs(ans - _count)
