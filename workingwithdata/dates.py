from datetime import datetime, timedelta

today = datetime.now()
print(' Today is: ' + str(today))

one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

# how do i extract some information of a chain?

print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))
