import calendar
def get_day_name(month, date, year):
    res = calendar.weekday(year, month, date)
    match res:
        case 0:
            return "MONDAY"
        case 1:
            return "TUESDAY"
        case 2:
            return "WEDNESDAY"
        case 3:
            return "THURSDAY"
        case 4:
            return "FRIDAY"
        case 5:
            return "SATURDAY"
        case 6:
            return "SUNDAY"