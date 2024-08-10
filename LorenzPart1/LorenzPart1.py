import numpy as np
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the Lorenz system
def lorenz(t, state, sigma, rho, beta):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Define the parameters and initial conditions
sigma = 10
rho = 28
beta = 8/3
initial_state = [1.001, 1, 1]  # introduce a small perturbation in the x variable
t_span = [0, 100]
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# Define the function to update the plot in the animation
def update_plot(i, solution, ax):
    ax.clear()
    ax.set_title("Lorenz Attractor")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.plot(solution[:, 0], solution[:, 1], solution[:, 2], color='blue', alpha=0.7)
    ax.plot(solution[i:i+10, 0], solution[i:i+10, 1], solution[i:i+10, 2], color='red', linewidth=3)

# Solve the differential equations using SciPy's solve_ivp function
solution = solve_ivp(lorenz, t_span, initial_state, args=(sigma, rho, beta), t_eval=t_eval)

# Plot an animated graph of the solution
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ani = FuncAnimation(fig, update_plot, frames=range(len(solution.t)), fargs=(solution.y.T, ax), interval=50, blit=False)
plt.show()
