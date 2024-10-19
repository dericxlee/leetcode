class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        visited = set()
        n = len(s)
        queue = deque([0])

        while queue:
            left = queue.popleft()

            if left in visited:
                continue

            visited.add(left)

            for right in range(left + 1, n+1):
                if s[left:right] in words:
                    if right == n:
                        return True

                    queue.append(right)
        
        return False