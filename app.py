import streamlit as st
from seir_model_with_decisions import seir_with_decisions, plot_seir
from economic_model import economic_collapse, plot_economy

st.title("Global Crisis Simulator")
st.sidebar.header("Pandemic Parameters")
N = st.sidebar.number_input("Population", value=1_000_000)
beta = st.sidebar.slider("Infection Rate (Beta)", 0.0, 1.0, 0.3)
sigma = st.sidebar.slider("Incubation Rate (Sigma)", 0.0, 1.0, 1/5.2)
gamma = st.sidebar.slider("Recovery Rate (Gamma)", 0.0, 1.0, 1/14)
days = st.sidebar.slider("Simulation Days", 30, 365, 180)
interventions = st.sidebar.text_input("Interventions (day,new_beta)", "30,0.1;90,0.2")
interventions = [(int(x.split(',')[0]), float(x.split(',')[1])) for x in interventions.split(';')]

st.sidebar.header("Economic Parameters")
gdp = st.sidebar.number_input("Initial GDP", value=1000)
unemployment = st.sidebar.number_input("Initial Unemployment (%)", value=5)
recovery_rate = st.sidebar.slider("Recovery Rate", 0.0, 0.1, 0.005)
econ_interventions = st.sidebar.text_input("Economic Interventions (day)", "30;90")
econ_interventions = [int(x) for x in econ_interventions.split(';')]

if st.button("Run Simulation"):
    # Pandemic simulation
    pandemic_result = seir_with_decisions(N-1, 1, 0, 0, beta, sigma, gamma, N, days, interventions)
    st.subheader("Pandemic Simulation")
    st.pyplot(plot_seir(pandemic_result, days))

    # Economic simulation
    economic_result = economic_collapse(gdp, unemployment, recovery_rate, econ_interventions, days)
    st.subheader("Economic Simulation")
    st.pyplot(plot_economy(economic_result, days))
