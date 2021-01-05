# Установка базового образа
FROM python:3.6

# Установка рабочей директории внутри контейнера и переход в нее
WORKDIR /app

# Копирование зависимостей
COPY requirements.txt .

# Установка pip и зависимостей
RUN pip install -U pip && pip install -r requirements.txt

# Копирование остальных файлов в /app
COPY . .

# Предустановка команда pytest и allure-отчёт
ENTRYPOINT ["pytest", "--alluredir", "allure-report"]

# Этот параметр можно переопределить при СОЗДАНИИ контейнера
CMD ["--browser_name", "chrome", "--browserVersion", "87.0"]
