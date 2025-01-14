from seir_model_with_decisions import seir_with_decisions, plot_seir
from economic_model import economic_collapse, plot_economy

# Pandemic parameters
N = 1_000_000
S, E, I, R = N - 1, 1, 0, 0
beta, sigma, gamma = 0.3, 1/5.2, 1/14
pandemic_days = 180
interventions = [(30, 0.1), (90, 0.2)]

# Economic parameters
gdp, unemployment = 1000, 5
recovery_rate = 0.005
economic_interventions = [30, 90]
economic_days = 180

# Simulate pandemic
pandemic_result = seir_with_decisions(S, E, I, R, beta, sigma, gamma, N, pandemic_days, interventions)
plot_seir(pandemic_result, pandemic_days)

# Simulate economy
economic_result = economic_collapse(gdp, unemployment, recovery_rate, economic_interventions, economic_days)
plot_economy(economic_result, economic_days)
