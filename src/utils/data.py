from utils import get_tmz_time


def extract_data(raw_data: dict, mapping: dict, station_id: int):
    """
    Extrai e transforma dados brutos em um formato específico de acordo com um mapeamento fornecido.

    Args:
        raw_data (dict): Dados não processados provenientes de fontes como FTPs e APIs.
        mapping (dict): Um dicionário que define como os campos de dados brutos devem ser mapeados
                        para campos específicos do resultado.
        station_id (int): O ID da estação à qual os dados estão associados.

    Returns:
        list: Uma lista de dicionários contendo os dados extraídos, formatados e mapeados.

    Note:
        A função `get_tmz_time` deve estar disponível e corretamente configurada para converter as datas e horas.
    """
    extracted_data_list = []

    # Extrair data e hora e combiná-los em um timestamp
    date_str = raw_data.get(mapping["date"])
    hour_str = raw_data.get(mapping["hour"])

    # Verifica se a data é a hora existe
    if date_str and hour_str:
        timestamp = get_tmz_time(date_str, hour_str)
    else:
        timestamp = "null"

    # Extrair variáveis
    for variable_id, variable_mapping in mapping["variables"].items():
        variable_data = {}

        for key, field in variable_mapping.items():
            if field and field in raw_data:
                variable_data[key] = raw_data[field]
            else:
                variable_data[key] = "null"

        # Construir o dicionário com os campos adicionais
        data_dict = {
            "data_hour": timestamp,
            "instant": variable_data.get("instant"),
            "maximun": variable_data.get("maximun"),
            "minimun": variable_data.get("minimun"),
            "average": variable_data.get("average"),
            "id_station": station_id,
            "id_variable": variable_id,
            "id_flag": 5,  # O valor padrão é 5
        }

        extracted_data_list.append(data_dict)

    return extracted_data_list
