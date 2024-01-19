# James Millerimport numpy as npimport matplotlib.pyplot as pltfrom scipy.integrate import solve_ivp# Function to get user input for a parameterdef userInput(prompt, default_value):    try:        return float(input(prompt))    except ValueError:        return default_value# Function to get user choice for computational loaddef getComputationalLoadChoice():    choices = {"low": 5, "medium": 10, "high": 15}    while True:        choice = input("Choose computational load (low, medium, high): ").lower()        if choice in choices:            return choices[choice]        else:            print("Invalid choice. Please enter 'low', 'medium', or 'high'.")# Ask the user for parametersk = userInput("Enter the efficiency of converting load to heat (k): ", 0.1)h = userInput("Enter the heat transfer coefficient (h): ", 0.05 * 9/5)T_ambient = userInput("Enter the ambient temperature (in Fahrenheit): ", 77)baseLoad = getComputationalLoadChoice()  # Get computational load choice from userdef graphicsCardComputationalLoad(t):    # Computer computational load function    return baseLoad + 5 * np.sin(t / 5)# ODE function def heatODE(t, T):    return k * graphicsCardComputationalLoad(t) - h * (T - T_ambient)# Time span for the simulation (e.g., 0 to 60 seconds)t_span = (0, 60)# Initial temperature of the graphics card (in Fahrenheit)T0 = [T_ambient]# Solving the ODE# solve_ivp is used to solve an initial value problem for a system of ODEs# heat_ode: The function representing the ODE# t_span: Tuple (start, end) defining the time interval over which to solve the ODE# T0: The initial condition (initial temperature)# t_eval: Points at which to store the computed solution, evenly spaced over the interval t_spansolution = solve_ivp(heatODE, t_span, T0, t_eval=np.linspace(t_span[0], t_span[1], 300))# Plottingplt.plot(solution.t, solution.y[0])plt.xlabel('Time in Seconds')plt.ylabel('Temperature in Fahrenheit')plt.title('Heat and Graphics Card Computation')plt.grid(True)plt.show()