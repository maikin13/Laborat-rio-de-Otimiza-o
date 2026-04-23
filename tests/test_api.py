from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_Health_check ():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'status': "ok", 'versao': "0.1.0"}

def test_resumo_sucesso ():
    dados = {'valores': [8.0, 10.0, 7.5, 9.0, 6.5]}
    response = client.post('/estatisticas/resumo', json = dados)
    assert response.status_code == 200
    assert "media" in response.json()
    assert response.json()["media"] == 8.2

def test_erroDP_400 ():
    dados = {'valores': [10.0, 10.0, 10.0]}
    response = client.post("/estatisticas/desvio-padrao", json = dados) 
    assert response.status_code == 400
    assert 'detail' in response.json()

def test_euclidiana_400 ():
    dados = {'vetor_a': [1.0, 2.0], 'vetor_b': [4.0, 5.0, 6.0]}
    response = client.post ("/vetores/distancia", json = dados)
    assert response.status_code == 422