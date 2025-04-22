import streamlit as st

st.title("🧪 Calculadora de Leyes de los Gases")
st.markdown("Selecciona una ley para calcular la variable que falta:")

# Selección de la ley
ley = st.selectbox("Ley a aplicar:", ["Ley de Boyle", "Ley de Charles", "Ley de Gay-Lussac"])

# Ley de Boyle
if ley == "Ley de Boyle":
    st.markdown("**P₁V₁ = P₂V₂** (Temperatura constante)")
    variable = st.selectbox("¿Qué variable deseas calcular?", ["P₁", "V₁", "P₂", "V₂"])
    if variable == "P₁":
        V1 = st.number_input("V₁ (L)", min_value=0.001)
        P2 = st.number_input("P₂ (atm)", min_value=0.001)
        V2 = st.number_input("V₂ (L)", min_value=0.001)
        if st.button("Calcular P₁"):
            P1 = (P2 * V2) / V1
            st.success(f"P₁ = {P1:.4f} atm")
    elif variable == "V₁":
        P1 = st.number_input("P₁ (atm)", min_value=0.001)
        P2 = st.number_input("P₂ (atm)", min_value=0.001)
        V2 = st.number_input("V₂ (L)", min_value=0.001)
        if st.button("Calcular V₁"):
            V1 = (P2 * V2) / P1
            st.success(f"V₁ = {V1:.4f} L")
    elif variable == "P₂":
        P1 = st.number_input("P₁ (atm)", min_value=0.001)
        V1 = st.number_input("V₁ (L)", min_value=0.001)
        V2 = st.number_input("V₂ (L)", min_value=0.001)
        if st.button("Calcular P₂"):
            P2 = (P1 * V1) / V2
            st.success(f"P₂ = {P2:.4f} atm")
    elif variable == "V₂":
        P1 = st.number_input("P₁ (atm)", min_value=0.001)
        V1 = st.number_input("V₁ (L)", min_value=0.001)
        P2 = st.number_input("P₂ (atm)", min_value=0.001)
        if st.button("Calcular V₂"):
            V2 = (P1 * V1) / P2
            st.success(f"V₂ = {V2:.4f} L")

# Ley de Charles
elif ley == "Ley de Charles":
    st.markdown("**V₁/T₁ = V₂/T₂** (Presión constante)")
    variable = st.selectbox("¿Qué variable deseas calcular?", ["V₁", "T₁", "V₂", "T₂"])
    if variable == "V₁":
        T1 = st.number_input("T₁ (K)", min_value=0.001)
        V2 = st.number_input("V₂ (L)", min_value=0.001)
        T2 = st.number_input("T₂ (K)", min_value=0.001)
        if st.button("Calcular V₁"):
            V1 = (V2 * T1) / T2
            st.success(f"V₁ = {V1:.4f} L")
    elif variable == "T₁":
        V1 = st.number_input("V₁ (L)", min_value=0.001)
        V2 = st.number_input("V₂ (L)", min_value=0.001)
        T2 = st.number_input("T₂ (K)", min_value=0.001)
        if st.button("Calcular T₁"):
            T1 = (V1 * T2) / V2
            st.success(f"T₁ = {T1:.4f} K")
    elif variable == "V₂":
        V1 = st.number_input("V₁ (L)", min_value=0.001)
        T1 = st.number_input("T₁ (K)", min_value=0.001)
        T2 = st.number_input("T₂ (K)", min_value=0.001)
        if st.button("Calcular V₂"):
            V2 = (V1 * T2) / T1
            st.success(f"V₂ = {V2:.4f} L")
    elif variable == "T₂":
        V1 = st.number_input("V₁ (L)", min_value=0.001)
        T1 = st.number_input("T₁ (K)", min_value=0.001)
        V2 = st.number_input("V₂ (L)", min_value=0.001)
        if st.button("Calcular T₂"):
            T2 = (V2 * T1) / V1
            st.success(f"T₂ = {T2:.4f} K")

# Ley de Gay-Lussac
elif ley == "Ley de Gay-Lussac":
    st.markdown("**P₁/T₁ = P₂/T₂** (Volumen constante)")
    variable = st.selectbox("¿Qué variable deseas calcular?", ["P₁", "T₁", "P₂", "T₂"])
    if variable == "P₁":
        T1 = st.number_input("T₁ (K)", min_value=0.001)
        P2 = st.number_input("P₂ (atm)", min_value=0.001)
        T2 = st.number_input("T₂ (K)", min_value=0.001)
        if st.button("Calcular P₁"):
            P1 = (P2 * T1) / T2
            st.success(f"P₁ = {P1:.4f} atm")
    elif variable == "T₁":
        P1 = st.number_input("P₁ (atm)", min_value=0.001)
        P2 = st.number_input("P₂ (atm)", min_value=0.001)
        T2 = st.number_input("T₂ (K)", min_value=0.001)
        if st.button("Calcular T₁"):
            T1 = (P1 * T2) / P2
            st.success(f"T₁ = {T1:.4f} K")
    elif variable == "P₂":
        P1 = st.number_input("P₁ (atm)", min_value=0.001)
        T1 = st.number_input("T₁ (K)", min_value=0.001)
        T2 = st.number_input("T₂ (K)", min_value=0.001)
        if st.button("Calcular P₂"):
            P2 = (P1 * T2) / T1
            st.success(f"P₂ = {P2:.4f} atm")
    elif variable == "T₂":
        P1 = st.number_input("P₁ (atm)", min_value=0.001)
        T1 = st.number_input("T₁ (K)", min_value=0.001)
        P2 = st.number_input("P₂ (atm)", min_value=0.001)
        if st.button("Calcular T₂"):
            T2 = (P2 * T1) / P1
            st.success(f"T₂ = {T2:.4f} K")
