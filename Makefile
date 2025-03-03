# Переменные для часто используемых команд
DC = docker-compose
DUP = $(DC) up -d
DDOWN = $(DC) down

# Основные команды
app_execute: docker_up_postgres docker_up_app docker_down_app docker_down_postgres

# Запуск PostgreSQL
docker_up_postgres:
	$(DUP) postgres

# Остановка PostgreSQL
docker_down_postgres:
	$(DDOWN) postgres

# Запуск приложения
docker_up_app:
	$(DUP) api

# Остановка приложения
docker_down_app:
	$(DDOWN) api

# Очистка
clean: clean_db

# Очистка базы данных
clean_db:
	rm -rf ./resources/*

# Проверка состояния контейнеров
status:
	$(DC) ps

# Логи PostgreSQL
logs_postgres:
	$(DC) logs postgres

# Логи приложения
logs_app:
	$(DC) logs api

# Указываем, что эти цели являются командами, а не файлами
.PHONY: app_execute docker_up_postgres docker_down_postgres docker_up_app docker_down_app clean clean_db status logs_postgres logs_app