#Какой язык программирования будем использовать
FROM python:latest

#Устанавливаем рабочую директорию
WORKDIR /app

#Копируем библиотеки в папку app
COPY requirements.txt .

#Устанавливаем все библиотеки
RUN pip install -r requirements.txt

#Копируем код проекта в контейнер
COPY . .

#Порт для нашего проекта
EXPOSE 8000

#Команда для запуска FastApi проекта
CMD ["uvicorn", "main:app", "--reload", "--port", "8000", "--host", "127.0.0.1"]

#Команда для сборки докер изображения
#docker build -t name_of_image .

#Команда для запуска изображения
#docker run -p 8000:8000 social_media_app
