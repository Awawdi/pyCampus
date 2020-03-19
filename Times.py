def gen_days(month, leap_year=True):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        yield 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        yield 31
    if month == 2 and not leap_year:
        yield 28
    if month == 2 and leap_year:
        yield 29


def gen_months():
    month = 1
    while month < 13:
        yield month
        month += 1


def gen_years(start=2019):
    while start < 2222:
        yield start
        start += 1


def gen_date():
    for y in gen_years():
        for m in gen_months():
            for d in gen_days(m):
                # yield str(h) + ":" + str(m) + ":" + str(s)
                yield '{:02d}/{:02d}/{:02d}'.format(d, m, y)


def gen_secs(seconds):
    i = 0
    while i < seconds:
        yield i
        i += 1


def gen_minutes(minutes):
    i = 0
    while i < minutes:
        yield i
        i += 1


def gen_hours(hours):
    i = 0
    while i < hours:
        yield i
        i += 1


def gen_time():
    # hours_gen = gen_hours()
    # minutes_gen = gen_minutes()

    for h in gen_hours(24):
        for m in gen_minutes(60):
            for s in gen_secs(60):
                # yield str(h) + ":" + str(m) + ":" + str(s)
                yield '{:02d}:{:02d}:{:02d}'.format(h, m, s)


def main():
    #for gt in gen_time():
    #   print(gt)

    #for gt_years in gen_years():
    #    print(gt_years)

    #for days_in_month in gen_days(1, False):
    #   print(days_in_month)

   for date in gen_date():
       for time in gen_time():
           print(date + " " + time)



main()
