import logging

def setup_logger():
    logger = logging.getLogger("app")
    logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования
    # Создаем обработчик, чтобы логи выводились в консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger
