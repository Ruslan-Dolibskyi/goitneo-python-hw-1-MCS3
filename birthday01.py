from datetime import datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    # Поточна дата
    today = datetime.today().date()

    # Структура для зберігання іменинників
    birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        # Отримання дати народження на цей рік
        birthday_this_year = birthday.replace(year=today.year)
        
        # Якщо день народження цього року вже пройшов, беремо дату на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Визначаємо скільки днів залишилося до дня народження
        delta_days = (birthday_this_year - today).days
        
        # Якщо день народження протягом наступного тижня
        if delta_days < 7:
            # Визначаємо день тижня
            weekday = birthday_this_year.strftime('%A')
            
            # Якщо це вихідний, переносимо на понеділок
            if weekday in ['Saturday', 'Sunday']:
                weekday = 'Monday'
            
            # Додаємо ім'я користувача до відповідного дня тижня
            birthdays[weekday].append(name)

    # Виведення результату
    for weekday, names in birthdays.items():
        print(f"{weekday}: {', '.join(names)}")


# Тестування
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 15)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 10, 13)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 14)},
    {"name": "Jan Koum", "birthday": datetime(1976, 10, 17)},
]
get_birthdays_per_week(users)
