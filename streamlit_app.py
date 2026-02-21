import streamlit as st
import joblib
import numpy as np

modelo = joblib.load("modelo_risco.pkl")

st.title("🎓 Previsão de Risco de Defasagem")

st.markdown("Modelo baseado nos indicadores educacionais.")

ida = st.number_input("IDA", 0.0, 10.0, 6.0)
ieg = st.number_input("IEG", 0.0, 10.0, 7.0)
iaa = st.number_input("IAA", 0.0, 10.0, 7.0)
ips = st.number_input("IPS", 0.0, 10.0, 7.0)
ipv = st.number_input("IPV", 0.0, 10.0, 7.0)

if st.button("Prever"):
    dados = np.array([[ida, ieg, iaa, ips, ipv]])
    
    prob = modelo.predict_proba(dados)[0][1]
    
    st.subheader(f"Probabilidade de Risco: {prob:.2%}")
    
    if prob > 0.5:
        st.error("⚠️ Alto risco de defasagem.")
    else:
        st.success("✅ Baixo risco.")