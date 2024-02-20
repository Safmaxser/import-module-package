from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
import emoji


if __name__ == '__main__':
    current_date = datetime.datetime.now().strftime('%d.%m.%Y')
    print(f'Текущая дата: {current_date}')
    result_emoji = emoji.emojize('Python это :thumbs_up:')
    print(result_emoji)
    calculate_salary()
    get_employees()
