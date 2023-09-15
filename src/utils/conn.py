import pysftp

from config import FTP_HOST, FTP_USER, FTP_PASS, FTP_PORT

def connect_sftp() -> pysftp.Connection:
    """
    Função para conectar a um servidor SFTP de dados.

    Returns:
        pysftp.Connection: Um objeto de conexão com o servidor SFTP.
    """
    # Indicando ao ftp não buscar uma chave SSH
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    # Criando objeto de conexão
    try:
        sftp = pysftp.Connection(
            host=FTP_HOST,
            username=FTP_USER,
            password=FTP_PASS,
            port=FTP_PORT,
            cnopts=cnopts,
        )
        # Retornando conexão
        return sftp

    except Exception as error:
        print(f"Erro ao conectar no SFTP: {error}")