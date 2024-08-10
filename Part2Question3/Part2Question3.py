# Part 2 Question 3

import numpy as np
import matplotlib.pyplot as plt

# Part a

# Define the range of values for p and k
p_vals = np.linspace(-10, 10, 1000)
k_vals = np.linspace(-10, 10, 1000)

# Create a 2D grid of p and k values
p, k = np.meshgrid(p_vals, k_vals)

# Define the inequality
ineq = (p * k) > p

# Create a plot of the inequality
plt.imshow(ineq, extent=[np.min(p_vals), np.max(p_vals), np.min(k_vals), np.max(k_vals)],
           origin='lower', cmap='Greys', alpha=0.5)

# Add labels and title
plt.xlabel('p')
plt.ylabel('k')
plt.title(r'$p*k > p$')

# Show the plot
plt.show()

# Part b

# Define the arrival rate range
x = np.linspace(0, 10, 1000)

# Define the factor k
k = 2

# Calculate the throughput for different arrival rates
throughput = x

# Calculate the new throughput with the factor k
new_throughput = k * x

# Plot the throughput vs arrival rate and new throughput vs arrival rate
plt.plot(x, throughput, label="Throughput")
plt.plot(x, new_throughput, label="New Throughput")

# Add labels and title
plt.xlabel('Arrival Rate')
plt.ylabel('Throughput')
plt.title('Throughput vs Arrival Rate with Factor k')

# Add legend
plt.legend()

# Show the plot
plt.show()

# Part c

# Define the arrival rate and service rate range
lambdas = np.linspace(0, 10, 1000)
mus = np.linspace(0, 10, 1000)

# Create a 2D grid of lambda and mu values
l, m = np.meshgrid(lambdas, mus)

# Calculate the old probability
Pold = l / m

# Calculate the new probability
Pnew = Pold / (1 - Pold)

# Create a plot of the new probability vs arrival rate and service rate
plt.imshow(Pnew, extent=[np.min(lambdas), np.max(lambdas), np.min(mus), np.max(mus)],
           origin='lower', cmap='inferno')

# Add labels and title
plt.xlabel('Arrival Rate (λ)')
plt.ylabel('Service Rate (μ)')
plt.title('New Probability vs Arrival and Service Rates')

# Show the plot
plt.colorbar()
plt.show()

# Part d

# Define the service rate and arrival rate range
lambdas = np.linspace(0, 10, 1000)
mus = np.linspace(0, 10, 1000)

# Create a 2D grid of lambda and mu values
l, m = np.meshgrid(lambdas, mus)

# Calculate the mean time in the system E[T]
ET = 1 / (m - l)

# Calculate the new E[T] with the factor k
k = 2
new_ET = (1 / (k * m)) * (1 / (m - l))

# Plot the E[T] vs arrival rate and service rate and new E[T] vs arrival rate and service rate
plt.imshow(ET, extent=[np.min(lambdas), np.max(lambdas), np.min(mus), np.max(mus)],
           origin='lower', cmap='inferno')
plt.imshow(new_ET, extent=[np.min(lambdas), np.max(lambdas), np.min(mus), np.max(mus)],
           origin='lower', cmap='coolwarm', alpha=0.5)

# Add labels and title
plt.xlabel('Arrival Rate (λ)')
plt.ylabel('Service Rate (μ)')
plt.title('Mean Time in System E[T] vs Arrival and Service Rates')

# Add colorbar and legend
plt.colorbar()
plt.legend(['E[T]', 'New E[T]'])

# Show the plot
plt.show()
