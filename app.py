# import pandas as pd
# import streamlit as st
# from seir_model_with_decisions import seir_with_decisions, plot_seir
#
# st.title("Global Crisis Simulator")
#
# # Input fields for simulation parameters
# S0 = st.number_input("Initial Susceptible Population:", min_value=0, value=1000)
# I0 = st.number_input("Initial Infected Population:", min_value=0, value=10)
# R0 = st.number_input("Initial Recovered Population:", min_value=0, value=0)
# days = st.number_input("Number of Days to Simulate:", min_value=1, value=100)
#
# # Decision thresholds for intervention
# thresholds = {
#     "infection_threshold": st.number_input("Infection Threshold:", min_value=1, value=500),
#     "recovery_threshold": st.number_input("Recovery Threshold:", min_value=1, value=500)
# }
#
# # Run SEIR model with decisions
# if st.button("Simulate Crisis"):
#     results = seir_with_decisions(S0, 0, I0, R0, 0.3, 0.1, 0.2, S0 + I0 + R0, days, thresholds)
#
#     # Display SEIR simulation results
#     st.write("SEIR Simulation Results")
#
#     # Check if results["I"] is in the expected format
#     if isinstance(results["I"], list):  # If it's a list
#         infected_data = pd.DataFrame(results["I"], columns=["Infected"])
#     else:
#         st.error("Infected data is not in the expected format.")
#         infected_data = pd.DataFrame()  # Empty DataFrame in case of error
#
#     # Plot infected data using line_chart
#     if not infected_data.empty:
#         st.line_chart(infected_data, caption="Infected Population Over Time")
#
#     # Plot other results
#     fig = plot_seir(results, days)
#     st.pyplot(fig)
#
#     # Display applied interventions history over time
#     st.subheader("Interventions Applied (Over Time):")
#     for intervention in results["interventions"]:
#         day = intervention["day"]
#         lockdown = "Yes" if intervention["lockdown"] else "No"
#         resource_allocation = "Yes" if intervention["resource_allocation"] else "No"
#         st.write(f"Day {day}: Lockdown: {lockdown}, Resource Allocation: {resource_allocation}")


import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from seir_model_with_decisions import seir_with_decisions, plot_seir

# Streamlit Title
st.title("Global Crisis: SEIR Model with Interventions")

# Sidebar inputs for SEIR parameters
st.sidebar.header("Initial Parameters")
S0 = st.sidebar.number_input("Initial Susceptible Population", min_value=1, value=1000)
E0 = st.sidebar.number_input("Initial Exposed Population", min_value=0, value=1)
I0 = st.sidebar.number_input("Initial Infected Population", min_value=0, value=1)
R0 = st.sidebar.number_input("Initial Recovered Population", min_value=0, value=0)

beta = st.sidebar.number_input("Transmission Rate (Beta)", min_value=0.0, value=0.3)
sigma = st.sidebar.number_input("Incubation Rate (Sigma)", min_value=0.0, value=0.2)
gamma = st.sidebar.number_input("Recovery Rate (Gamma)", min_value=0.0, value=0.1)
N = S0 + E0 + I0 + R0  # Total population

# Sidebar for Intervention Thresholds
st.sidebar.header("Intervention Thresholds")
infection_threshold = st.sidebar.number_input("Infection Threshold", min_value=0, value=50)
recovery_threshold = st.sidebar.number_input("Recovery Threshold", min_value=0, value=100)
thresholds = {
    "infection_threshold": infection_threshold,
    "recovery_threshold": recovery_threshold
}

# Sidebar for number of days to run the simulation
days = st.sidebar.number_input("Number of Days for Simulation", min_value=1, value=100)

# Run simulation when button is pressed
if st.sidebar.button("Run Simulation"):
    # Run SEIR model with decisions
    results = seir_with_decisions(S0, E0, I0, R0, beta, sigma, gamma, N, days, thresholds)

    # Plot SEIR results
    fig = plot_seir(results, days)
    st.pyplot(fig)

    # Show the final population states after the simulation
    st.write(f"Final Susceptible Population after {days} days: {results['S'].iloc[-1]:.0f}")
    st.write(f"Final Exposed Population after {days} days: {results['E'].iloc[-1]:.0f}")
    st.write(f"Final Infected Population after {days} days: {results['I'].iloc[-1]:.0f}")
    st.write(f"Final Recovered Population after {days} days: {results['R'].iloc[-1]:.0f}")

    # Display interventions applied over time
    st.subheader("Interventions Applied Over Time")
    interventions_df = pd.DataFrame(results["interventions"])
    st.write(interventions_df)
