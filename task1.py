import datetime

date = "2026-09-24"

def get_days_from_today(date):
    try:
        current_datetime = datetime.datetime.today()
        specific_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        specific_date = specific_date.date()
        current_datetime = current_datetime.date()
        difference = current_datetime - specific_date
        return difference.days
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None
print(get_days_from_today(date))