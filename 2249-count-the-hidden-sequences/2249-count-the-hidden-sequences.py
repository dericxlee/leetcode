class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        floor, ceiling = float('inf'), float('-inf')
        pref = 0

        for diff in differences:
            pref += diff
            floor = min(floor, pref)
            ceiling = max(ceiling, pref)
        
        if ceiling > 0:
            lower += ceiling
        if floor < 0:
            upper += floor

        return upper - lower + 1 if upper >= lower else 0
    
