import calendar
import locale

print(locale.getlocale())
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
print(calendar.calendar(2024))
