# Graphics Card Temperature Simulation

## Project Overview

This project simulates the temperature of a graphics card under different computational loads over time. The simulation is based on solving an Ordinary Differential Equation (ODE) that models the heat dynamics of a graphics card.

## Programmer

- James Miller

## Code Packages Used

- `numpy`: Used for numerical operations.
- `matplotlib`: Utilized for plotting the temperature curve.
- `scipy.integrate`: Employed for solving the ODE.

## Approach to Implementation

### ODE Equation

The core of the simulation is based on the following ODE, which models the temperature dynamics:

\[ \frac{dT(t)}{dt} = k \cdot P(t) - h \cdot (T(t) - T_{\text{ambient}}) \]

Where:
- \( T(t) \) is the temperature of the graphics card at time \( t \).
- \( \frac{dT(t)}{dt} \) represents the rate of change of temperature over time.
- \( k \) is a constant for the efficiency of converting computational load to heat.
- \( P(t) \) is the computational load at time \( t \).
- \( h \) is the heat transfer coefficient.
- \( T_{\text{ambient}} \) is the ambient temperature.

### Key Components

1. **User Input for Parameters**: The program prompts the user to input various parameters, including the efficiency of converting computational load to heat (`k`), the heat transfer coefficient (`h`), the ambient temperature, and the computational load level (low, medium, high).

2. **Computational Load Function**: Based on the user's choice, the program sets a computational load level, which affects the rate of temperature change.

3. **ODE Definition and Solution**: An ODE function (`heat_ode`) defines the relationship between the temperature, the computational load, and the cooling efficiency. The `scipy.integrate.solve_ivp` function solves this ODE.

4. **Visualization**: The results are visualized using `matplotlib`, displaying how the temperature of the graphics card evolves over time.

### Program Flow

1. Gather user inputs.
2. Define the ODE based on the inputs.
3. Solve the ODE over a specified time interval.
4. Plot the results to visualize the temperature change over time.

## How to Run

Ensure you have Python installed with the required packages (`numpy`, `matplotlib`, `scipy`). Run the script from the command line or an IDE.
