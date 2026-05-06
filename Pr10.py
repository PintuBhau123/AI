import random
import math

def objective(x):
    return x**2

def simulated_annealing():
    current = random.uniform(-10, 10)
    temperature = 100
    cooling = 0.95

    while temperature > 1:
        new = current + random.uniform(-1, 1)

        cost_diff = objective(new) - objective(current)

        if cost_diff < 0 or random.random() < math.exp(-cost_diff / temperature):
            current = new

        temperature *= cooling

    return current

# Driver code
result = simulated_annealing()
print("Approximate solution:", result)
print("Minimum value:", result**2)
print("Jayant75")