# Simple function to maximize
def f(x):
    return -(x ** 2) + 4 * x

def hill_climb(start):
    current = start

    # peak at x = 2
    while True:
        neighbors = [current - 1, current + 1]   # left & right
        next_node = max(neighbors, key=f)

        if f(next_node) <= f(current):
            return current   # reached peak

        current = next_node

result = hill_climb(0)
print("Best solution:", result)
print("Maximum value:", f(result))
print("Jayant")