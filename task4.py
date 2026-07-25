import datetime

def get_upcoming_birthdays(users):
    today = datetime.datetime.now().date()
    upcoming_birthdays = []

    for user in users:
        birthday_date = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday_date.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        days_between = (birthday_this_year - today).days
        if 0 <= days_between <= 7:
            congratulation_date = birthday_this_year
            if congratulation_date.weekday() == 5: # Субота
                congratulation_date += datetime.timedelta(days=2)
            elif congratulation_date.weekday() == 6: # Неділя
                congratulation_date += datetime.timedelta(days=1)
            upcoming_birthdays.append({
            "name": user["name"],
            "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users = [
    {"name": "Alice", "birthday": "2026.05.15"},
    {"name": "Bob", "birthday": "2026.06.20"},
    {"name": "Charlie", "birthday": "2026.04.10"},
    {"name": "David", "birthday": "2026.07.25"},
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)