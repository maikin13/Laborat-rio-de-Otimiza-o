from pydantic import BaseModel, Field, model_validator
from typing import List

class ListaValores(BaseModel):
    valores: List[float] = Field(

        ...,
        min_length = 1,
        description = "Lista de valores numéricos (reais)."

    )

    model_config = {

        "json_schema_extra": {
            "examples": [
                {
                    "valores": [8.0, 10.0, 7.5, 9.0, 6.5]
                }
            ]
        }
    }

class ListaValoresDP(BaseModel):
    valores: List[float] = Field(

        ...,
        min_length = 2,
        description = "Lista de valores de Desvio Padrão (mínimo 2)"
    )

class DoisVetores(BaseModel):
    vetor_a: List[float] = Field(..., min_length = 1, description = "Primeiro vetor")
    vetor_b: List[float] = Field(..., min_length = 1, description = "Segundo vetor")

    @model_validator(mode = "after")
    def verificar_tamanhos_iguais (self):
        if len(self.vetor_a) != len(self.vetor_b):
            raise ValueError ("Os dois vetores devem ter o mesmo tamanho.")
        return self

    model_config = {
        "json_schema_extra": {
            'examples': [

            {

                "vetor_a": [1.0, 2.0, 3.0],
                "vetor_b": [4.0, 5.0, 6.0]

            }
            ]  
        }
    }

class Resumo(BaseModel):
    media: float
    mediana: float
    minimo: float
    maximo: float
    amplitude: float
    variancia: float
    desvio_padrao: float