class Solution:
    def countLargestGroup(self, n: int) -> int:
        group = defaultdict(int)
        largest_size = 0
        num_groups = 0

        for i in range(1, n+1):
            sum = 0
            while i > 0:
                sum += i % 10
                i //= 10
            
            group[sum] += 1

            if group[sum] > largest_size:
                largest_size = group[sum]
                num_groups = 1
            elif group[sum] == largest_size:
                num_groups += 1
        
        return num_groups