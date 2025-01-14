import matplotlib.pyplot as plt
import pandas as pd

def seir_with_decisions(S0, E0, I0, R0, beta, sigma, gamma, N, days, thresholds):
    S, E, I, R = [S0], [E0], [I0], [R0]
    interventions_history = []  # To track interventions over time

    for day in range(1, days):
        # Apply SEIR model equations
        new_infected = beta * S[-1] * I[-1] / N
        new_recovered = gamma * I[-1]

        # Apply interventions if conditions are met
        interventions = simulate_decisions({"I": I, "R": R}, thresholds)

        # Update compartments with interventions considered
        S.append(S[-1] - new_infected)
        E.append(E[-1] + new_infected - sigma * E[-1])
        I.append(I[-1] + sigma * E[-1] - new_recovered)
        R.append(R[-1] + new_recovered)

        # Store interventions along with the day
        interventions_history.append({
            "day": day,
            "lockdown": interventions["lockdown"],
            "resource_allocation": interventions["resource_allocation"]
        })

    # Convert results to pandas DataFrame for easier plotting with Streamlit
    results = {
        "S": pd.Series(S),
        "E": pd.Series(E),
        "I": pd.Series(I),
        "R": pd.Series(R),
        "interventions": interventions_history  # Save the full history of interventions
    }

    return results

def simulate_decisions(results, thresholds):
    interventions = {"lockdown": False, "resource_allocation": False}

    # Print current infected and recovered values for debugging
    print(f"Current Infected: {results['I'][-1]}, Infection Threshold: {thresholds['infection_threshold']}")
    print(f"Current Recovered: {results['R'][-1]}, Recovery Threshold: {thresholds['recovery_threshold']}")

    # If infected population exceeds a threshold, apply interventions
    if results["I"][-1] > thresholds["infection_threshold"]:
        interventions["lockdown"] = True
        interventions["resource_allocation"] = True

    # Optionally, implement other rules for decision-making
    if results["R"][-1] < thresholds["recovery_threshold"]:
        interventions["resource_allocation"] = True

    # Display the intervention results to the user
    if interventions["lockdown"]:
        print("Lockdown applied.")
    else:
        print("Lockdown not applied.")

    if interventions["resource_allocation"]:
        print("Resource allocation applied.")
    else:
        print("Resource allocation not applied.")

    return interventions

def plot_seir(results, days):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["S"], label="Susceptible")
    ax.plot(results["E"], label="Exposed")
    ax.plot(results["I"], label="Infected")
    ax.plot(results["R"], label="Recovered")
    ax.set_xlabel("Days")
    ax.set_ylabel("Population")
    ax.set_title("SEIR Model")
    ax.legend()
    ax.grid()
    return fig
