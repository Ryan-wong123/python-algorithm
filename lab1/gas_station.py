import heapq

def min_stops(D, M, S):
    S.append(D)  # Treat destination as last "station"
    num_stops = 0
    current_fuel = M
    prev = 0
    max_heap = []

    for station in S:
        distance = station - prev

        # Refuel from best previous stations if we can't reach the next one
        while current_fuel < distance:
            if not max_heap:
                return -1  # No station to refuel from
            current_fuel += -heapq.heappop(max_heap)
            num_stops += 1

        current_fuel -= distance

        # After reaching this station, we can consider refueling here
        if station != D:
            heapq.heappush(max_heap, -M)

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
