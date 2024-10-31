class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0

        tail = None

        for interval in intervals:
            if tail == None or tail <= interval[0]:
                tail = interval[1]
                print(tail)
            else:
                count+=1
        
        return count