import datetime
from collections import Counter

def calcular_diferenca_em_minutos(inicio, fim):
    # Converte as strings de data e hora para objetos datetime
    inicio = datetime.datetime.strptime(inicio, "%Y-%m-%d %H:%M:%S")
    fim = datetime.datetime.strptime(fim, "%Y-%m-%d %H:%M:%S")

    # Calcula a diferença em segundos e converte para minutos
    diferenca = fim - inicio
    return diferenca.total_seconds() / 60

def main():
    tempos = []

    
    with open("entrada.txt", "r") as arquivo:# Lê o arquivo de entrada
        for linha in arquivo:
            # Divide a linha em 2 pares de data e hora
            dados = linha.strip().split(" a ")
            inicio, fim = dados[0], dados[1]

            # Calcula o tempo de atendimento em minutos e adiciona na lista
            tempo_minutos = calcular_diferenca_em_minutos(inicio, fim)
            tempos.append(tempo_minutos)

    # Cálculo do mínimo e máximo
    minimo = min(tempos)
    maximo = max(tempos)

    # Cálculo da moda
    contador = Counter(tempos)
    moda = [tempo for tempo, freq in contador.items() if freq == max(contador.values())]

    # Se a moda tem mais de um valor, imprime -1
    if len(moda) > 1:
        moda = -1
    else:
        moda = moda[0]

    # Cálculo da média
    media = sum(tempos) / len(tempos)

    # Impressão dos resultados
    print(f"{minimo:.1f}")
    print(f"{maximo:.1f}")
    print(f"{moda:.1f}" if moda != -1 else -1)
    print(f"{media:.1f}")

if __name__ == "__main__":
    main()