import numpy as np
from itertools import product

# Define states and transition matrix
states = ['Sunny', 'Cloudy', 'Rainy']
transition_matrix = np.array([
    [0.6, 0.3, 0.1],  # Sunny -> Sunny, Cloudy, Rainy
    [0.4, 0.4, 0.2],  # Cloudy -> Sunny, Cloudy, Rainy
    [0.2, 0.3, 0.5]   # Rainy -> Sunny, Cloudy, Rainy
])

# Function to simulate Markov process
def simulate_markov_weather(initial_state, num_days):
    current_state = initial_state
    state_sequence = [current_state]
    state_indices = {state: idx for idx, state in enumerate(states)}
    
    for _ in range(num_days):
        current_idx = state_indices[current_state]
        next_state = np.random.choice(states, p=transition_matrix[current_idx])
        state_sequence.append(next_state)
        current_state = next_state
    
    return state_sequence

# Simulate 10 days starting from Sunny
initial_state = 'Sunny'
num_days = 10
weather_sequence = simulate_markov_weather(initial_state, num_days)
print(f"Weather sequence for {num_days} days starting from {initial_state}:")
print(" -> ".join(weather_sequence))

# Calculate probability of at least 3 rainy days in 10 days
# We'll use matrix exponentiation to get the n-step transition probabilities

# Function to calculate probability of at least k rainy days in n steps
def prob_at_least_k_rainy_days(start_state, n, k):
    # Initialize state vector
    state_idx = states.index(start_state)
    state_vector = np.zeros(len(states))
    state_vector[state_idx] = 1
    
    # Initialize count of rainy days
    total_prob = 0
    
    # We need to consider all possible sequences with at least k rainy days
    # This is complex, so we'll use Monte Carlo simulation for estimation
    num_simulations = 10000
    count = 0
    
    for _ in range(num_simulations):
        sequence = simulate_markov_weather(start_state, n)
        rainy_days = sequence.count('Rainy')
        if rainy_days >= k:
            count += 1
    
    return count / num_simulations

prob = prob_at_least_k_rainy_days('Sunny', 10, 3)
print(f"\nProbability of at least 3 rainy days in 10 days starting from Sunny: {prob:.4f}")
