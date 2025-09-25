import logging
from os import path


def setup_logger(logger_name, log_file, level=logging.DEBUG):
    # Definindo o caminho absoluto para o arquivo de log
    log_file_path = path.join(path.dirname(__file__), log_file)

    # Cria um logger separado
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # Evita duplicação de handlers
    if not logger.hasHandlers():
        # Formatação dos logs
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # FileHandler para salvar os logs em arquivo
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)

        # Adiciona o handler ao logger
        logger.addHandler(file_handler)

    return logger
