Projeto para disciplina de Laboratório de Otimização -
Autoria : Michael Cauan

É uma API *stateless* desenvolvida para receber dados numéricos, calcular métricas estatísticas e retornar os resultados em formato JSON.

## Tecnologias Utilizadas:
*Python*
*FastAPI:* Framework para a construção da API.
*Pydantic:* Validação rigorosa dos dados de entrada.
*Uvicorn:* Servidor ASGI para rodar a aplicação
*Pytest e TestClient:* Bateria de testes automatizadas

## Como executar o projeto;

**1. Crie e ative o ambiente virtual:**

- No windows:
  python -m venv .venv
  .venv\Scripts\activate

- No Linux/Mac:
  python -m venv .venv
  source .venv/bin/activate


**2. Instale as dependências exigidas:**

pip install -r requirements.txt

**3. Inicie o servidor local:**

python -m uvicorn src.api:app --reload

- Com o servidor rodando, a documentação interativa (Swagger) estará disponível no seu navegador em:
 http://localhost:8000/docs

Nesta interface gráfica, você poderá testar facilmente todos os endpoints de cálculo (Média, Mediana, Desvio Padrão, Resumo Completo e Distância Euclidiana).

**3.1 Como Rodar os Testes:**
O projeto conta com mais de 8 testes automatizados para validar as regras de negócio, cálculos matemáticos e os retornos dos endpoints (incluindo falhas esperadas).
Para executá-los, pare o servidor (pressionando Ctrl+C no terminal) e rode o comando:

python -m pytest -v