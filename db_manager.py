import psycopg2
from config import config


class DBManager:

    def __init__(self, params):
        self.conn = psycopg2.connect(**params)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий у каждой компании
        :return:
        """
        self.cur.execute(
            """SELECT e.company_name, count(v.vacancy_id) FROM employers AS e 
            INNER JOIN vacancies as v
            USING (employer_id)
            GROUP BY employer_id
            ORDER BY e.company_name"""
        )
        rows = self.cur.fetchall()
        return rows

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию
        :return:
        """
        self.cur.execute(
            """SELECT v.job_title, e.company_name, v.salary, v.job_url 
            FROM vacancies AS v
            INNER JOIN employers AS e 
            USING (employer_id)"""
        )
        rows = self.cur.fetchall()
        return rows[0][0]

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям
        :return:
        """
        self.cur.execute("""SELECT CEILING(AVG(salary)) FROM vacancies""")
        rows = self.cur.fetchall()
        return rows[0][0]

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий, у которых зарплата выше средней по
        всем вакансиям
        :return:
        """
        self.cur.execute(
            """SELECT job_title 
            FROM vacancies
            WHERE salary > (SELECT CEILING(AVG(salary)) 
            FROM vacacies)"""
        )
        rows = self.cur.fetchall()
        return rows

    def get_vacancies_with_keyword(self, keyword):
        """
        Получает список всех вакансий, в названии которых содержатся
        переданные в метод слова, например python
        :param keyword: ключевое слово для получение списка
        :return:
        """
        list_keyword = keyword.split()
        str_keyword = '%'.join(list_keyword)

        self.cur.execute(
            """SELECT job_title 
            FROM vacancies
            WHERE job_title LIKE %s""",
            ('%'+str_keyword+'%', )
        )
        rows = self.cur.fetchall()
        self.conn.close()
        return rows

    def closes_the_connection_to_the_database(self):
        self.cur.close()
        self.conn.close()
