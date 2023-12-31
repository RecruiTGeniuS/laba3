# Проверить, что строка является синтаксически 
# корректным СНИЛС.
# Сама регулярка ^([0-9]{3})(\-)([0-9]{3})(\-)([0-9]{3})(\s)([0-9]{2})$

import re


# Функция для проверки
def check(m):
    if m != None:
        return "Строка - синтаксически корректный СНИЛС(v)"
    else:
        return "Строка - не синтаксически корректный СНИЛС(-)"

# Тестовые строки
test_string = {
    "445-444-332 45",
    "Привет",
    "444444444",
    "23423-333-222-11",
    "43-43-43 52"
    "444-222-111 50",
    "43423412251",
    "123-снисл-123-33-12",
    "441-223-123 70",
    "777-123-431 80",
    "123-412-4444444",
    "1",
    "186-234-312 77",
    "987-765-309 23",
    "312-412-785342 11"
}

# Регулярное выражение
reg = r'^([0-9]{3})(\-)([0-9]{3})(\-)([0-9]{3})(\s)([0-9]{2})$'

for string in test_string:
    match = re.search(reg, string)
    print(f"{string} : {check(match)}")
    print("-----------------------------------------------------")