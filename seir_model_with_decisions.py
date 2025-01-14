import matplotlib.pyplot as plt


def seir_with_decisions(S, E, I, R, beta, sigma, gamma, N, days, interventions):
    """
    Includes dynamic interventions (e.g., lockdowns).
    Parameters:
        interventions: List of tuples (day, new_beta)
    """
    S_vals, E_vals, I_vals, R_vals = [S], [E], [I], [R]
    interventions = sorted(interventions, key=lambda x: x[0])  # Sort interventions by day

    for day in range(days):
        # Check for interventions
        for intervention_day, new_beta in interventions:
            if day == intervention_day:
                beta = new_beta

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
