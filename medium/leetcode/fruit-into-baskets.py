class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        first = -1
        second = -1
        #[1,2,1,1,1,3,3,3,3,,3,3,3,3]
        fruitsIChose = defaultdict(int)
        j = 0
        mx = 0
        curr = 0
        while j < len(fruits):
            mx = max(curr, mx)
            fruitsIChose[fruits[j]] = curr+1
            if len(fruitsIChose) > 2:
                mx = max(curr, mx)
                curr -= fruitsIChose[first]
                fruitsIChose[second] -= fruitsIChose[first]
                fruitsIChose.pop(first)
                first = fruits[j]
                first, second = second, first
            curr += 1
            mx = max(curr, mx)
            fruitsIChose[fruits[j]] = curr
            if first == -1:
                first = fruits[j]
            elif second == -1 and first!=fruits[j]:
                second = fruits[j]
            elif second != fruits[j] and second != -1:
                second, first = first, second
            j += 1
        return mx