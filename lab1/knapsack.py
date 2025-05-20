class Item:
    def __init__(self, weight=0, value=0):
        self.weight = weight
        self.value = value
        self.ratio = 0.0

def fractional_knapsack(W, items, n):
    # Step 1: Compute value-to-weight ratio
    for item in items:
        item.ratio = item.value / item.weight

    # Step 2: Sort by highest value/weight ratio
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0.0
    for item in items:
        if W == 0:
            break
        if item.weight <= W:
            # Take the whole item
            total_value += item.value
            W -= item.weight
        else:
            # Take a fraction of the item
            total_value += item.ratio * W
            W = 0

    return total_value

def main():
    # Input number of items and capacity
    n, W = map(int, input("Enter number of items and knapsack capacity, separated by space: ").split())

    # Input weights
    weights = list(map(int, input("Enter the weights for each item (separated by spaces): ").split()))

    # Input values
    values = list(map(int, input("Enter the values for each item (separated by spaces): ").split()))

    # Construct list of Item objects
    items = [Item(weight=weights[i], value=values[i]) for i in range(n)]

    # Solve the knapsack problem
    max_value = fractional_knapsack(W, items, n)

    print(f"Maximum value that can be carried: {max_value:.2f}")

if __name__ == "__main__":
    main()
