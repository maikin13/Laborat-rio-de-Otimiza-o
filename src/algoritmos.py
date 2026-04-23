import math
import statistics

#Cálculo da média
def calcular_media (valores: list[float]) -> float:
    return statistics.mean(valores)

#Cálculo da Mediana
def calcular_mediana(valores: list[float]) -> float:
    return statistics.median(valores)

#Desvio-padrão 
def calcular_dp (valores: list[float]) -> float:
    if len(set(valores)) == 1:
        raise ValueError("Todos os valores são iguais. O desvio padrão é zero e inválido.")
    
    return statistics.stdev(valores)

#Cálculo do restante do resumo estatístico.
def calcular_resumo (valores: list[float]) -> dict:
    minimo = min(valores)
    maximo = max(valores)
    amplitude = maximo - minimo 
    variancia = statistics.variance(valores) if len(valores) > 1 else 0.0
    desvio = statistics.stdev(valores) if len(set(valores)) > 1 else 0.0

    return {
    'media': calcular_media(valores),
    'mediana': calcular_mediana(valores),
    'minimo': minimo,
    'maximo': maximo,
    'amplitude': amplitude,
    'variancia': variancia,
    'desvio_padrao': desvio
    
}

def dist_euclidiana(vetor_a: list[float], vetor_b: list[float]) -> float:
    '''Calcula a distancia euclidiana entre dois vetores do mesmo tamanho'''
    return math.dist(vetor_a, vetor_b)

def multiplicar_escalar(valores: list[float], escalar: float) -> list[float]:
    """Multiplica uma lista de valores por um escalar. """
    return [valor * escalar for valor in valores]