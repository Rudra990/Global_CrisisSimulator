from seir_model import seir_model, plot_seir

# Initial parameters
N = 1_000_000  # Total population
S = N - 1  # Initially susceptible
E = 1       # Initially exposed
I = 0       # Initially infected
R = 0       # Initially recovered
beta = 0.3  # Infection rate
sigma = 1/5.2  # Incubation rate (1/average incubation days)
gamma = 1/14   # Recovery rate (1/average infection duration)
days = 180     # Simulation period in days

# Run simulation
result = seir_model(S, E, I, R, beta, sigma, gamma, N, days)

# Plot results
plot_seir(result, days)
