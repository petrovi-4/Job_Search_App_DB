import psycopg2

from config import config
from db_manager import DBManager
from utils import (
    get_info_about_employers, get_vacancies, create_database,
    create_employers_table, create_vacancies_table,
    insert_data
)

list_employers_id = [78638, 3529, 2324020, 2180, 5008932, 83639, 1057,
                     946607, 4934, 1204987]


def main():
    employers = get_info_about_employers(list_employers_id)

    vacancies = {}
    key = 1
    for employer_id in list_employers_id:
        vacancies[key] = get_vacancies(employer_id)
        key += 1

    params = config()
    db_name = 'my_db'

    create_database(params, db_name)
    print("База данных успешно создана")
    params.update({'dbname': db_name})

    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                create_employers_table(cur)
                print('Таблица employers создана успешно')
                create_vacancies_table(cur)
                print('Таблица vacancies создана успешно')
                insert_data(cur, employers, vacancies)
                print('Данные в таблицы добавлены успешно')
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    print('\nСписок компаний и количество вакансий у каждой компании:')
    request_1 = DBManager(params).get_companies_and_vacancies_count()
    for row in request_1:
        print(f'{row[0]} - {row[1]}')

    print('\nСписок всех вакансий:')
    request_2 = DBManager(params).get_all_vacancies()
    for row in request_2:
        print(row)

    print('\nСредняя зарплата по вакансиям:')
    request_3 = DBManager(params).get_avg_salary()
    print(request_3)

    print(
        '\nСписок всех вакансий, у которых зарплата выше средней по всем '
        'вакансиям:'
    )
    request_4 = DBManager(params).get_vacancies_with_higher_salary()
    for row in request_4:
        print(row[0])

    keyword = 'Python разработчик'
    print(f'\nСписок всех вакансий в которых содержится "{keyword}":')
    request_5 = DBManager(params).get_vacancies_with_keyword(keyword)
    for row in request_5:
        print(row[0])

    DBManager(params).closes_the_connection_to_the_database()


if __name__ == '__main__':
    main()
