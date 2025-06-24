import sys

def coin_change(coins, amount):
    # Initialize DP array: default to inf, except dp[0] = 0
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # Build up from 1 to amount
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>", file=sys.stderr)
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            if not lines:
                print("File is empty.", file=sys.stderr)
                sys.exit(1)

            amount = int(lines[0].strip())

            if len(lines) < 2:
                print("No coin values provided.", file=sys.stderr)
                sys.exit(1)

            coin_values = list(map(int, lines[1].strip().split()))
    except FileNotFoundError:
        print(f"Error opening file: {filename}", file=sys.stderr)
        sys.exit(1)
    except ValueError:
        print("File content is not in the expected format.", file=sys.stderr)
        sys.exit(1)

    result = coin_change(coin_values, amount)
    print(result)

if __name__ == "__main__":
    main()
