import os

# === Константы для подключения к Базам Данных ===
MONGO_DB_NAME = "files"
DATABASE_URL = None
DATABASE_MONGO_URL = None

# === Инициализация переменных зависимых от среды ===
env = os.getenv('CONTEXT_ENVIRONMENT', 'local')
if env == 'docker':
    # === Подключение внутри контейнера ===
    pg_user = os.getenv('POSTGRES_USER')
    pg_passwd =  os.getenv('POSTGRES_PASSWORD')
    pg_host = os.getenv('POSTGRES_HOST')
    pg_port = os.getenv('POSTGRES_PORT')
    pg_db = os.getenv('POSTGRES_DB')
    mongo_user = os.getenv('MONGO_USER')
    mongo_passwd =  os.getenv('MONGO_PASSWORD')
    mongo_host = os.getenv('MONGO_HOST')
    mongo_port = os.getenv('MONGO_PORT')
    mongo_db = os.getenv('MONGO_DB')
    
    DATABASE_URL = f'postgresql://{pg_user}:{pg_passwd}@{pg_host}:{pg_port}/{pg_db}'
    DATABASE_MONGO_URL = f'mongodb://{mongo_user}:{mongo_passwd}@{mongo_host}:{mongo_port}/{mongo_db}?authSource=admin'
    
elif env == 'local':
    # === Подключение к контейнерам ===
    DATABASE_URL = 'postgresql://fast_api:root@localhost:5445/bankDB'
    DATABASE_MONGO_URL = 'mongodb://fast_api:root@localhost:27018/fileStorageDB?authSource=admin'
