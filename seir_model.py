import numpy as np
import matplotlib.pyplot as plt


# SEIR Model function
def seir_model(S, E, I, R, beta, sigma, gamma, N, days):
    """
    Parameters:
        S: Initial susceptible population
        E: Initial exposed population
        I: Initial infected population
        R: Initial recovered population
        beta: Infection rate
        sigma: Incubation rate (1/incubation period)
        gamma: Recovery rate (1/infection period)
        N: Total population
        days: Number of days to simulate
    Returns:
        A dictionary of daily values for S, E, I, R
    """
    S_vals, E_vals, I_vals, R_vals = [S], [E], [I], [R]

    for _ in range(days):
        dS = -beta * S * I / N
        dE = beta * S * I / N - sigma * E
        dI = sigma * E - gamma * I
        dR = gamma * I

        S += dS
        E += dE
        I += dI
        R += dR

        S_vals.append(S)
        E_vals.append(E)
        I_vals.append(I)
        R_vals.append(R)

    return {
        "Susceptible": S_vals,
        "Exposed": E_vals,
        "Infected": I_vals,
        "Recovered": R_vals,
    }


# Plot results
def plot_seir(data, days):
    plt.figure(figsize=(10, 6))
    plt.plot(data["Susceptible"], label="Susceptible")
    plt.plot(data["Exposed"], label="Exposed")
    plt.plot(data["Infected"], label="Infected")
    plt.plot(data["Recovered"], label="Recovered")
    plt.xlabel("Days")
    plt.ylabel("Population")
    plt.title("SEIR Model Simulation")
    plt.legend()
    plt.grid()
    plt.show()
