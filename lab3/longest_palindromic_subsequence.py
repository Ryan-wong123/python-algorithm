import sys

def longest_palindromic_subsequence(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters
    for i in range(n):
        dp[i][i] = 1

    # Build the DP table
    for length in range(2, n + 1):  # length of substring
        for i in range(n - length + 1):
            j = i + length - 1  # ending index

            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <input_string_file>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            input_string = file.read().strip()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        sys.exit(1)

    result = longest_palindromic_subsequence(input_string)
    print(result)


if __name__ == "__main__":
    main()

