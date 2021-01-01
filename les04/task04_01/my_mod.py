def calculate(worked_time=0, hourly_rate=0, bonus=0):
    try:
        return float(worked_time) * float(hourly_rate) + float(bonus)
    except TypeError:
        return
