import numpy as np
import matplotlib.pyplot as plt

def economic_collapse(gdp, unemployment, recovery_rate, intervention_days, days):
    """
    Simulates economic decline and recovery.
    Parameters:
        gdp: Initial GDP (arbitrary units)
        unemployment: Initial unemployment rate (percentage, 0-100)
        recovery_rate: Rate of recovery per day
        intervention_days: List of days where interventions occur (stimulus packages)
        days: Total days to simulate
    Returns:
        A dictionary of daily GDP and unemployment rates
    """
    gdp_vals, unemployment_vals = [gdp], [unemployment]
    intervention_effect = 0.05  # % GDP growth per intervention

    for day in range(days):
        # Simulate natural decline
        gdp -= gdp * 0.01  # 1% daily GDP loss
        unemployment += 0.2  # 0.2% daily unemployment rise

        # Apply intervention effects
        if day in intervention_days:
            gdp += gdp * intervention_effect
            unemployment -= 1  # Reduce unemployment by 1%

        # Recovery phase
        gdp += gdp * recovery_rate
        unemployment = max(0, unemployment - recovery_rate * 10)

        gdp_vals.append(gdp)
        unemployment_vals.append(unemployment)

    return {
        "GDP": gdp_vals,
        "Unemployment": unemployment_vals,
    }

def plot_economy(data, days):
    plt.figure(figsize=(10, 6))
    plt.plot(data["GDP"], label="GDP")
    plt.plot(data["Unemployment"], label="Unemployment Rate (%)", linestyle="--")
    plt.xlabel("Days")
    plt.ylabel("Metrics")
    plt.title("Economic Collapse and Recovery Simulation")
    plt.legend()
    plt.grid()
    plt.show()
