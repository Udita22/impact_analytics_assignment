class GraduationCeremony:
    def __init__(self, n):
        self.n = n

    def validWays(self):
        n = self.n
        dp = [[0 for _ in range(5)] for _ in range(n + 1)]

        # Initialization for the 0th day
        for i in range(4):
            dp[0][i] = 1

        for i in range(1, n+1):
            for j in range(4):
                dp[i][j] = dp[i-1][0] + dp[i-1][j+1]

        valid_ways_to_attend_classes = dp[n][0]
        ways_to_miss_last_day = dp[n-1][1]

        return f"{ways_to_miss_last_day}/{valid_ways_to_attend_classes}"

if __name__ == "__main__":
    n = int(input("Enter the value of N "))
    graduationCeremonyObj = GraduationCeremony(n)
    output = graduationCeremonyObj.validWays()

    print(output)