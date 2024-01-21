import numpy as npfrom scipy.integrate import odeintimport matplotlib.pyplot as plt# Define the Queue Length ODE functiondef queueLength(Q, t, arrival_rate, processing_rate):    dQdt = arrival_rate - processing_rate * Q    return dQdt# Prompt the user for input or use defaultsprint("Queue Length ODE Solver")# Prompt the user for arrival rate (tasks per unit time)arrivalRateInput = input("Enter the arrival rate (tasks per unit time, e.g., 2.0), or press Enter to use the default (2.0): ")if arrivalRateInput:    arrivalRate = float(arrivalRateInput)else:    arrivalRate  = 2.0  # Default arrival rate# Prompt the user for processing rate (tasks per unit time)processingRateInput = input("Enter the processing rate (tasks per unit time, e.g., 1.0), or press Enter to use the default (1.0): ")if processingRateInput:    processingRate = float(processingRateInput)else:    processingRate = 1.0  # Default processing rate# Time points for the solutiont = np.linspace(0, 10, 100)  # Example time range from 0 to 10 units# Solve the Queue Length ODEinitial_queue_length = 0  # Initial queue lengthsolution = odeint(queueLength, initial_queue_length, t, args=(arrivalRate , processingRate))# Visualize the solutionplt.figure(figsize=(8, 6))plt.plot(t, solution, label='Queue Length')plt.xlabel('Time (Seconds)')plt.ylabel('Queue Length (Tasks)')plt.title('Queue Length over Time')plt.legend()plt.grid(True)plt.show()