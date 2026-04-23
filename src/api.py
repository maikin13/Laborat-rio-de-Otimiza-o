from fastapi import FastAPI, Query, Path, HTTPException
from src import ListaValores, ListaValoresDP, DoisVetores, Resumo
from src import algoritmos

app = FastAPI( 
    
    title = "API de Laboratório de Otimização",
    description = 'API para cálculos estatísticos básicos.',
    version = '0.1.0'

)

@app.get("/", tags=["Health"])
def health_check():
    return {'status': 'ok', 'versao': '0.1.0' }  

@app.post('/estatisticas/resumo', tags = ['Estatísticas'],  response_model = Resumo)
def resumo_completo(dados: ListaValores, decimais: int = Query(2, ge = 0, le = 6)):
    try:
        resultado = algoritmos.calcular_resumo(dados.valores)
        return {k: round(v, decimais) for k, v in resultado.items()}
    
    except Exception:
        raise HTTPException (status_code = 500, detail = "Erro interno de processamento!.")  

@app.post('/estatisticas/media', tags = ['Estatísticas'])
def calcular_media (dados: ListaValores):
    return {'media': algoritmos.calcular_media(dados.valores)}

@app.post('/estatisticas/mediana', tags = ['Estatísticas'])
def calcular_mediana(dados: ListaValores):
    return {'mediana': algoritmos.calcular_mediana(dados.valores)}

@app.post('/estatisticas/desvio-padrao', tags = ['Estatísticas'])
def calcular_dp (dados: ListaValoresDP):
    try:
        resultado = algoritmos.calcular_dp(dados.valores)
        return {'desvio_padrao': resultado}
    except ValueError as e:
        raise HTTPException(status_code = 400, detail = str(e))
    except Exception:
        raise HTTPException(status_code = 500, detail = "Erro interno inesperado.")

@app.post('/vetores/distancia', tags = ['Vetores'])
def calcular_euclidiana(dados: DoisVetores):
    try:
        resultado = algoritmos.dist_euclidiana(dados.vetor_a, dados.vetor_b)
        return {'distancia': resultado}
    except Exception:
        raise HTTPException(status_code = 500, detail = 'Erro interno inesperado.')

@app.post('/vetores/escalar/{valor}', tags = ['Vetores'])
def multiplicar_escalar(

    dados: ListaValores,
    valor: float = Path(..., description = "Valor escalar para multiplicar a lista.")

): 
    resultado = algoritmos.multiplicar_escalar(dados.valores, valor)
    return {'resultado': resultado}