# Описание
Приложение [Job_Search_App_DB](https://github.com/petrovi-4/Job_Search_App_DB.git) производит поиск вакансий по списку выбранных компаний из API сайта hh.ru и сохраняет результат в базу данных.  
Из базы данных можно получить: 
 
	- список всех компаний и количество вакансий у каждой компании,
	- список всех вакансий,
	- среднюю зарплату по вакансиям,
	- вакансии с зарплатой выше средней,
	- поиск вакансии по клбчевым словам

## Запуск проекта
**Клонировать репозиторий:**

```
git@github.com:petrovi-4/Job_Search_App_DB.git
```

**Создать и активировать виртуальное окружение:**

```
poetry init
```

**Установка зависимостей:**

```
poetry install
```

**Создать файл database.ini в папке проекта по образцу:** 

```
[postgresql]
host=localhost
user=<имя_пользователя>
password=<пароль>
port=<порт> 
```

**Запуск проекта**

```
python main.py
```

**Автор**  
[Мартынов Сергей](https://github.com/petrovi-4)

![GitHub User's stars](https://img.shields.io/github/stars/petrovi-4?label=Stars&style=social)
![licence](https://img.shields.io/badge/licence-GPL--3.0-green)