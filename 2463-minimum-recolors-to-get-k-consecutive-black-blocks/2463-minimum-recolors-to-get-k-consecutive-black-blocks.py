class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        counter = Counter(blocks[:k])
        result = counter["W"]

        for i in range(k, len(blocks)):
            counter[blocks[i]] = counter.get(blocks[i], 0) + 1
            counter[blocks[i-k]] -= 1

            result = min(result, counter["W"])
        
        return result
