class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        colors = defaultdict(int)
        rabbits = 0

        for answer in answers:
            match = answer + 1

            if match not in colors:
                rabbits += match
            
            colors[match] += 1
            
            if colors[match] >= match:
                del colors[match]
        
        return rabbits
