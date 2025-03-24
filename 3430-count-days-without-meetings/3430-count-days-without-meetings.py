class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        sorted_meetings = sorted(meetings, key=lambda x:x[0])
        time = 0
        result = 0

        for start, end in sorted_meetings:
            if start > time + 1:
                result += start - time - 1
            
            time = max(time, end)
        
        return result + days - time