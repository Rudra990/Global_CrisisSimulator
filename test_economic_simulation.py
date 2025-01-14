from economic_model import economic_collapse, plot_economy

# Initial parameters
gdp = 1000  # Arbitrary GDP units
unemployment = 5  # Initial unemployment rate (%)
recovery_rate = 0.005  # 0.5% GDP recovery per day
intervention_days = [30, 90]  # Stimulus packages
days = 180  # Simulation period

# Run simulation
result = economic_collapse(gdp, unemployment, recovery_rate, intervention_days, days)

# Plot results
plot_economy(result, days)
