from datetime import date
class DateRange:
    def __contains__(self, item):
        pass
birth_year = input('what year you were born?')

age = 2020 - int(birth_year)

print(f' you are is: {age}')