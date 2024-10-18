class TrieNode:
    def __init__(self):
        self.children = {}
        self.final = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.count = 0

    def _insert(self, subarray: list):
        node = self.root
        for num in subarray:
            if num not in node.children:
                self.count += 1
                node.children[num] = TrieNode()
            node = node.children[num]

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        trie = Trie()
        n = len(nums)

        for i in range(n):
            div = 0
            arr = []

            for j in range(i, n):
                arr.append(nums[j])

                if nums[j] % p == 0:
                    div += 1
                
                if div > k:
                    break
                
                trie._insert(arr)
        
        return trie.count

        