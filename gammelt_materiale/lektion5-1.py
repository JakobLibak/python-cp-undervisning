# Vi vil gerne spørge om hvornår en person er født
# og derefter regne personens alder ud.

from datetime import date

def calculate_age(birth_date):
    ''' Expected in YYYY-MM-DD format '''
    today = date.today()
    age = today.year - birth_date.year
    # full_year_passed = (today.month, today.day) < (birth_date.month, birth_date.day)
    full_year_passed = today < birth_date.replace(2020)
    print(today)
    print(birth_date.month)
    # full_year_passed = (today.month + today.day) < (birth_date.month, birth_date.day)
    print(full_year_passed)
    if not full_year_passed:
        age -= 1
    return age

datoinput = date(1978, 1, 19)
datoinput2 = datoinput.replace(1980)

print(datoinput2)
# print(datoinput.year)
# print(date.today().month)

# test1 = (datoinput.month * 12) +  datoinput.day
# print(test1)

alder1 = calculate_age(datoinput)
print(alder1)

# dato = date.today()

# print(dato)