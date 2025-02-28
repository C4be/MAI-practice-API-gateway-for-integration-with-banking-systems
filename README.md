# MAI-practice-API-gateway-for-integration-with-banking-systems

Разработка API-шлюза для интеграции с банковскими системами

---

# Техническое задание

## Цель и функциональные требования
- [ ] Разработать API-шлюз для взаимодействия с банковскими системами:
  - [ ] ДБО (Дистанционное банковское обслуживание) – для загрузки документов клиентами.
  - [ ] АБС (Автоматизированная банковская система) – для хранения и
обработки документов.
  - [ ] СМ (Система управления) – для привязки документов к карточкам контрактов.
- [ ] Обеспечить защиту API с использованием OAuth 2.0/JWT.
- [ ] Разработать версионность API для поддержки будущих изменений.
## Выходные артефакты
- [ ] Документ со схемой API, описанием эндпоинтов и форматов запросов.
- [ ] Прототип API-шлюза (FastAPI, PostgreSQL).
- [ ] Тестовый сценарий передачи документов между сервисами.

---

# План выполнения работ

Приведенный ниже план разбит на этапы с метриками для контроля прогресса.

#### **Этап 1: Проектирование**

**Задачи**:

1. **Анализ требований**:
   - [ ] Уточнить форматы данных для ДБО, АБС, СМ (JSON/XML, спецификации полей).
   - [ ] Определить роли пользователей и права доступа (например, клиент, администратор).
   - [ ] Согласовать версионность (например, `v1`, `v2` в URL).

2. **Схема API**:
   - [ ] Описать эндпоинты для каждой системы:
     - [ ] ДБО: Загрузка документов (`POST /v1/dbo/documents`).
     - [ ] АБС: Получение статуса документа (`GET /v1/abs/documents/{id}`).
     - [ ] СМ: Привязка к контракту (`POST /v1/sm/contracts/{id}/link`).
   - [ ] Форматы запросов/ответов (пример на OpenAPI 3.0).

3. **Архитектура**:
   - [ ] Выбрать FastAPI + PostgreSQL.
   - [ ] Спроектировать базу данных (ER-диаграмма).
   - [ ] Решить, как хранить JWT (краткосрочные токены с рефреш-токенами).

**Метрики**:
- [ ] Документ с OpenAPI-спецификацией.
- [ ] ER-диаграмма БД.
- [ ] Подписание ТЗ заказчиком.

#### **Этап 2: Разработка базового функционала**

**Задачи**:

1. **Настройка проекта**:
   - [ ] Инициализация FastAPI.
   - [ ] Подключение PostgreSQL через SQLAlchemy.
   - [ ] Настройка Alembic для миграций.

2. **Реализация безопасности**:
   - [ ] OAuth2 с JWT: эндпоинт `/token`.
   - [ ] Middleware для проверки токенов.
   - [ ] Ролевая модель (например, `client`, `admin`).

3. **Базовые эндпоинты**:
   - [ ] ДБО: Загрузка документов (сохранение в БД + заглушка для АБС).
   - [ ] АБС: Мок-реализация хранения документов.
   - [ ] СМ: Привязка документа к контракту (проверка существования ID).

**Метрики**:
- [ ] Рабочий прототип на локальной машине.
- [ ] 80% покрытие кода unit-тестами (pytest).
- [ ] Успешная аутентификация через Postman.

#### **Этап 3: Интеграция с системами**

**Задачи**:

1. **Интеграция с ДБО**:
   - [ ] Реализация загрузки файлов (PDF, DOCX) в хранилище (например, MinIO/S3).
   - [ ] Валидация форматов (макс. размер 10 МБ, разрешенные типы).

2. **Интеграция с АБС**:
   - [ ] Реализация синхронизации статусов документов (например, `pending`, `approved`).
   - [ ] Шина событий (Celery/RabbitMQ) для асинхронной обработки.

3. **Интеграция с СМ**:
   - [ ] Привязка документа к карточке контракта (проверка прав доступа).
   - [ ] Логирование операций (например, через Elasticsearch).

**Метрики**:
- [ ] Успешная передача документа из ДБО в АБС.
- [ ] Отображение статуса документа в АБС через API.
- [ ] 100% интеграционных тестов (pytest + Docker).

---

#### **Этап 4: Тестирование и оптимизация**

**Задачи**:

1. **Нагрузочное тестирование**:
   - [ ] Проверка на 100 RPS (например, Locust).
   - [ ] Оптимизация запросов к БД (индексы, кэширование через Redis).

2. **Безопасность**:
   - [ ] Проверка на уязвимости (OWASP ZAP/Snyk).
   - [ ] Валидация входных данных (например, pydantic-модели).

3. **Документация**:
   - [ ] Swagger/Redoc для API.
   - [ ] Руководство для разработчиков (примеры запросов).

**Метрики**:
- [ ] Время отклика < 500 мс на 90% запросов.
- [ ] Отсутствие критических уязвимостей.
- [ ] Документация опубликована на SwaggerHub.

---

### **Стек технологий**
- **Backend**: FastAPI, SQLAlchemy, Pydantic.
- **База данных**: PostgreSQL + Redis (кэш).
- **Безопасность**: OAuth2, JWT, Let’s Encrypt.
- **Инфраструктура**: Docker, Kubernetes, AWS.
- **Тестирование**: pytest, Postman, Locust.