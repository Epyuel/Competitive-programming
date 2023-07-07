class Solution:
    def frequencySort(self, s: str) -> str:
        num = Counter(s)
        ans = ""
        for l, count in num.most_common():
            ans += l*count
        return ans
