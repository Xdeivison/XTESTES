import os

# Confgurações do FTP
FTP_HOST = os.environ.get("FTP_HOST") # Endereço do servidor
FTP_USER = os.environ.get("FTP_USER") # Nome do usuario
FTP_PASS = os.environ.get("FTP_PASS") # Senha de acesso
FTP_PORT = os.environ.get("FTP_PORT") # Porta da conexão