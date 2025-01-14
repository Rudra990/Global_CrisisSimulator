from seir_model_with_decisions import seir_with_decisions, plot_seir

# Initial parameters
N = 1_000_000
S = N - 1
E = 1
I = 0
R = 0
beta = 0.3
sigma = 1/5.2
gamma = 1/14
days = 180

# Interventions: Lockdown at day 30 reduces beta to 0.1
interventions = [(30, 0.1), (90, 0.2)]

# Run simulation
result = seir_with_decisions(S, E, I, R, beta, sigma, gamma, N, days, interventions)

# Plot results
plot_seir(result, days)
