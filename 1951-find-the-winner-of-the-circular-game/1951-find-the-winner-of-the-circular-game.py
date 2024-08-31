class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n+1))
        count = k

        while len(friends) > 1:
            count-=1
            
            if count == 0:
                friends.pop(0)
                count = k
            else:
                friends.append(friends.pop(0))
            
        return friends[0]
                


