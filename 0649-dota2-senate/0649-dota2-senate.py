class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        freq = Counter(list(senate))
        queue = deque(list(senate))

        banDire, banRad = 0, 0

        while freq["D"] and freq["R"]:
            senator = queue.popleft()

            if banDire and senator == "D":
                banDire -= 1
                freq["D"] -= 1
                continue
            if banRad and senator == "R":
                banRad -= 1
                freq["R"] -= 1
                continue
            
            if senator == "R":
                banDire += 1
            else:
                banRad += 1
            
            queue.append(senator)

        return "Radiant" if queue.popleft() == "R" else "Dire"

