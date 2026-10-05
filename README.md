### Проект GQB

## Описание проекта
Booking - это тестовый проект с применением LLM для ответов пользователям по вопросам бронирования отелей.

Проект загружен на удаленный репозиторий и доступен по адресу - https://booking-uk8s.onrender.com/


## Используемые технологии
*Проект реализован с использованием следующего функционала*: 
- Python 3.12
- FastAPI 0.141.1 
- Groq 1.6.0 (языковая модель: Groq API, модель llama-3.3-70b-versatile)


Все необходимые для работы Booking зависимости перечислены в requirements.txt
Рекомендуется перед установкой развернуть виртуальное окружение с верисей python 3.12:

Bash:
```
py -3.12 -m venv venv 
```

Для установки зависимостей необходимо выполнить команду:
```
pip install -r requirements.txt
```


## Команда проекта
Проект создан в качесте тестового задания.  
Над проектом работал [Андрей Дубов](https://github.com/Andrey-Dubov-25)  


## Ссылка на проект
[Проект Booking](https://github.com/Andrey-Dubov-25/booking)

### Как запустить проект:

**Локально**

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Andrey-Dubov-25/booking
```

```
cd booking
```


Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```


Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```


Запустить проект:

```
uvicorn app.main:app --reload
```