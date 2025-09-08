url = "https://viacep.com.br/ws/04729030/json/" #importa o dicionário
import requests


r = requests.get(url)
print (r.json()['regiao'])
print (r.json())

endereco = {
  "cep": "03685-020",
  "logradouro": "Rua Morro de Santa Teresa",
  "bairro": "Jardim São Nicolau",
  "localidade": "São Paulo",
  "uf": "SP",
  "estado": "São Paulo",
  "regiao": "Sudeste",
}


print(endereco['bairro'])

