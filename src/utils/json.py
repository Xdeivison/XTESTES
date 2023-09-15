import os
import json
import logging
import pandas as pd

from config import DATA_DIR


def handle_exceptions(func: callable):
    """
    Um decorador que lida com exceções específicas durante a execução de uma função.

    Este decorador envolve a função passada como argumento em um bloco try-except e registra erros
    específicos que podem ocorrer durante a execução da função.

    Args:
        func (callable): A função que será decorada.

    Returns:
        callable: A função decorada.
    """
    def wrapper(*args, **kwargs):
        # Tenta executar a função passada como argumento
        try:
            return func(*args, **kwargs)
        
        except FileNotFoundError as fnf_error:
            # Registra um erro se um arquivo ou pasta não for encontrado
            logging.error(f"Erro: Pasta ou arquivo não encontrado - {fnf_error}")

        except json.JSONDecodeError as json_decode_error:
            # Registra um erro se houver um erro de decodificação JSON
            logging.error(f"Erro ao decodificar JSON: {json_decode_error}")

        except pd.errors.EmptyDataError as empty_data_error:
            # Registra um erro se um DataFrame estiver vazio
            logging.error(f"Erro: DataFrame vazio - {empty_data_error}")

        except Exception as error:
            # Registra um erro genérico se ocorrer qualquer outra exceção não tratada
            logging.error(f"Erro desconhecido: {error}")

    return wrapper


@handle_exceptions
def save_json(data: pd.DataFrame, file_name: str) -> None:
    """
    Salva um DataFrame em formato JSON.

    Args:
        dataframe (DataFrame): Um DataFrame contendo os dados das estações.
        file_name (str): O nome do arquivo no qual os dados serão salvos.
    """
    # Cria o caminho completo para o arquivo
    dir = os.path.join(DATA_DIR, file_name)  

    # Converte o DataFrame para JSON
    json_str = data.to_json(orient="records", indent=4)  

    # Escreve o JSON no arquivo
    with open(dir, "w") as file:
        file.write(json_str)  


@handle_exceptions
def load_json(file_path: str) -> list:
    """
    Carrega dados de um arquivo JSON a partir de um caminho especificado.

    Args:
        file_path (str): O caminho do arquivo JSON a ser carregado.

    Returns:
        list: Uma lista contendo os dados carregados do arquivo JSON.
    """
    # Cria o caminho completo para o arquivo
    dir = os.path.join(DATA_DIR, file_path) 

    # Carrega o JSON do arquivo
    with open(dir, "r") as file_json:
        data = json.load(file_json)  

    # Retorna os dados carregados do arquivo JSON
    return data  

