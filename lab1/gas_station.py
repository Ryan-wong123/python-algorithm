import heapq

def min_stops(D, M, S):
    S.append(D)
    num_stops = 0
    current_fuel = M
    prev = 0
    max_heap = []

    for station in S:
        distance = station - prev

        # Refuel while we can't reach the next station
        while current_fuel < distance:
            if not max_heap:
                return -1
            # Refuel from the best previous station
            current_fuel += -heapq.heappop(max_heap)
            num_stops += 1
            # Clear the heap (as in first version)
            max_heap = []

        current_fuel -= distance

        # Push remaining fuel (M - current_fuel) at this station
        if station != D:
            remaining = M - current_fuel
            heapq.heappush(max_heap, -remaining)

        prev = station

    return num_stops

# DO NOT change anything below this line for Gradescope
if __name__ == "__main__":
    D = int(input("Enter the total distance (D): "))
    M = int(input("Enter the maximum fuel range (M): "))
    S = list(map(int, input("Enter the distances of the gas stations separated by spaces: ").split()))
    result = min_stops(D, M, S)
    if result == -1:
        print("Destination is not reachable.")
    else:
        print(f"Minimum number of stops: {result}")
