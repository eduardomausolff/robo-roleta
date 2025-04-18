
import random
import time

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

if __name__ == "__main__":
    while True:
        resultado = girar_roleta()
        print(f"Resultado: {resultado}")
        print(analisar_tendencia())
        time.sleep(2)  # Pausa de 2 segundos entre cada rodada
