class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        cur = [0] * k
        min_unfairness = float('inf')

        def dfs(i, zero_count):
            nonlocal min_unfairness

            if n - i < zero_count: return

            if i == n:
                max_cookies = max(cur)
                min_unfairness = min(min_unfairness, max_cookies)
                return

            for j in range(k):
                zero_count -= int(cur[j] == 0)
                cur[j] += cookies[i]
                dfs(i + 1, zero_count)
                cur[j] -= cookies[i]
                zero_count += int(cur[j] == 0)

        dfs(0, k)
        return min_unfairness
