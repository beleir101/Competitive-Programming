class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        maximum = 0
        for i in range(len(blocks)):
            if i + k > len(blocks):
                break
            c = blocks[i:i+k]
            d = c.count("B")
            if d > maximum:
                maximum = d
        return k - maximum