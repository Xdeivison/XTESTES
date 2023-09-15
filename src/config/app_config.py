import os
import pytz

# Configurações de PATH
APP_URL = os.environ.get("APP_URL")   # URL para requisição do banco de dados
DATA_DIR = os.environ.get("DATA_DIR") # Caminho para salvar os dados baixados
LOGS_DIR = os.environ.get("LOGS_DIR") # Caminho para salvar os logs dos scripts

# Configuração de fuso-horario
TIME_ZONE = pytz.timezone('America/Sao_Paulo')
