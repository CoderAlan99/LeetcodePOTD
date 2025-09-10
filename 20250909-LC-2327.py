# 2327 - Number of People Aware of a Secret

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        """
        dp = no. of NEW people who learn the secret
        in Context delay=2, forget=4
        dp[1] = 1 (Instantiated for person A)
        dp[3] = 1 (Person A told a new person B)
        dp[4] = 1 (Person A told a new person C)
        dp[5] = 1 (Person B told a new person D)
        # Note that at dp[5], person A will forget the secret
        """
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            # People can share from j = max(1, i - forget + 1) to i - delay
            left = max(1, i - forget + 1)
            right = i - delay
            if right >= left:
                dp[i] = sum(dp[left:right + 1]) % MOD
            else:
                dp[i] = 0
            # print(dp)

        # Sum last 'forget' days (people who haven't forgotten)
        return sum(dp[max(1, n - forget + 1):n + 1]) % MOD
