
import streamlit as st
import random

st.set_page_config(page_title="Robô da Roleta", layout="centered")

cores = ['vermelho', 'preto', 'verde']
historico = []

def girar_roleta():
    resultado = random.choices(cores, weights=[18, 18, 1])[0]
    historico.append(resultado)
    return resultado

def analisar_tendencia():
    if len(historico) < 5:
        return "Aguardando mais dados..."
    ultimos = historico[-5:]
    tendencia = max(set(ultimos), key=ultimos.count)
    return f"Tendência: {tendencia.upper()} (últimos 5: {ultimos})"

st.title("Roleta Brasileira - Analisador")
st.markdown("Simule os giros e veja a tendência com base nos últimos resultados.")

if st.button("Girar Roleta"):
    resultado = girar_roleta()
    st.success(f"Resultado: {resultado}")
    st.info(analisar_tendencia())

if historico:
    st.subheader("Histórico Completo")
    st.write(historico)
