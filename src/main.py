"""
Esta função executa as seguintes etapas:
1. Obtém a data atual.
2. Calcula o horário UTC atual usando a função get_utc_time().
3. Gera um nome de arquivo JSON usando a data e o horário.
4. Chama a função get_data_times() para obter os dados das estações automáticas do INMET.
5. Chama a função save_json() para salvar os dados em um arquivo JSON.
6. Imprime os dados obtidos.
"""
import datetime as dt
import logging
import schedule
import time

from app import get_data_times, get_data_manuals
from utils import save_json, get_utc_time

# Configurando o sistema de LOG
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

"""
    Variáveis Globais
        - date (str): Data atual (formato "YYYY-MM-DD")
        - previous_date (str): Data anterior há uma semana
        - hour (str): Horário da consulta (formato "HHMM")
"""

# Obtém a data atual
date = dt.datetime.today().date()

# Data anterior há uma semana
previous_date = date - dt.timedelta(weeks=1)

# Obtém o horário atual em formato UTC usando a função 'get_utc_time' do módulo 'utils'
hour = get_utc_time()

def main():
    """
    Obtém os dados das estações automáticas  do INMET, com base na data atual e hora.
    """
    # Define o nome dos arquivo com base na data atual e hora
    file_name = f"inmet{date}_{hour}.json"

    # Obtém os dados das estações automáticas do INMET com base na data e hora
    time_data = get_data_times(date, hour)
    print(time_data)

    # Salva os dados em formato JSON no arquivo especificado
    save_json(time_data, file_name)

    return 0

def main1():
    """
    Obtém os dados das estações manuais do INMET, com base na data atual e na data anterior há uma semana
    """
    # Define o nome dos arquivo com base na data atual e na data anterior
    file_name_manuals = f"inmet{date}_{previous_date}.json"

    # Obtém os dados do INMET (estações MANUAIS) com base na data atual e na anterior há uma semana
    data_manuals = get_data_manuals(date, previous_date)
    print(data_manuals)

    # Salva os dados em formato JSON no arquivo especificado
    save_json(data_manuals, file_name_manuals)

    return 0

if __name__ == "__main__":
    # Agendando main() para rodar a cada hora, começando 15 minutos após a hora
    schedule.every().hour.at(":15").do(main)

    # Agendando main1() para rodar toda segunda-feira às 3 da manhã
    schedule.every().monday.at("03:00").do(main1)

    while True:
        schedule.run_pending()
        time.sleep(60)
