# Part 2 Question 1
import numpy as np
import matplotlib.pyplot as plt

# Define the start time data
start = [1, 3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 10, 12.41, 12.82, 13.28, 14.65, 15]

# Plot start time data
plt.scatter(start, range(1, 16))
plt.xlabel('Start Time')
plt.ylabel('Arrival Time')
plt.title('Arrival Time VS Start Time')
plt.show()

# Define exit time data
exit = [3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 9.58, 12.41, 12.82, 13.28, 14.65, 14.92, 15.27]

# Plot exit time data
plt.scatter(exit, range(1, 16))
plt.xlabel('Exit Time')
plt.ylabel('Arrival Time')
plt.title('Arrival Time VS Exit Time')
plt.show()

# Define time in queue data
time_in_queue = [0, 1.22, 1.98, 3.11, 2.25, 2.01, 1.71, 1.18, 0.4, 0, 1.41, 0.82, 0.28, 0.65, 0]

# Plot time in queue data
plt.scatter(time_in_queue, range(1, 16))
plt.xlabel('Time in Queue')
plt.ylabel('Arrival Time')
plt.title('Arrival Time VS Time in Queue')
plt.show()

# Define customers in system data
customers_in_system = [0, 1, 2, 2, 2, 3, 4, 3, 2, 0, 1, 2, 1, 1, 0]

# Plot the customers in system data
plt.scatter(customers_in_system, range(1, 16))
plt.xlabel('Amount of Customers in System')
plt.ylabel('Arrival Time')
plt.title('Arrival time VS Amount of Customers in System')
plt.show()

# Define customers in queue data
customers_in_queue = [0, 0, 1, 1, 1, 2, 3, 2, 1, 0, 0, 1, 0, 0, 0]

# Plot the customers in queue data
plt.scatter(customers_in_queue, range(1, 16))
plt.xlabel('Amount of Customers in Queue')
plt.ylabel('Arrival Time')
plt.title('Arrival time VS Amount of Customers in Queue')
plt.show()
