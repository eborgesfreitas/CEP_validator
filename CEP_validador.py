import requests
import json

def CEP_validador(cep_original):
    """
        Consulta a API do ViaCEP para obter informações de endereço.
    """
    # 1. Limpar o CEP: remover hífens e espaços em branco
    cep = str(cep_original).replace('-', '').strip()

    # 2. Validando o cep
    if not cep.isdigit() or len(cep) != 8:
        print("CEP inválido. Por favor, insira um CEP de 8 dígitos numéricos (com ou sem hífen).")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"

    print(f"Consultando CEP: {cep}...")
    try:
        response = requests.get(url)

        dados_cep = response.json()

        if "erro" in dados_cep:
            print(f"CEP '{cep}' não encontrado ou inválido.")
        else:
            print("\n--- Detalhes do Endereço ---")
            print(f"CEP: {dados_cep.get('cep')}")
            print(f"Logradouro: {dados_cep.get('logradouro')}")
            print(f"Bairro: {dados_cep.get('bairro')}")
            print(f"Cidade: {dados_cep.get('localidade')}")
            print(f"Estado: {dados_cep.get('estado')}")
            print(f"UF: {dados_cep.get('uf')}")
            print(f"DDD: {dados_cep.get('ddd')}")
            print(f"Região: {dados_cep.get('regiao')}")
            print("----------------------------")
            return dados_cep

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API do ViaCEP: {e}")
    except json.JSONDecodeError:
        print("Erro ao decodificar a resposta JSON da API.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

CEP_validador(24240670)
