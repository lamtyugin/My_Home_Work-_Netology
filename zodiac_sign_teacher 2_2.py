signs = {"март": (21, "Рыбы", "Овен"), "апрель": (21, "Овен", "Телец"), "май": (22, "Телец", "Близнецы"),
        "июнь": (22, "Близнецы", "Рак"), "июль": (23, "Рак", "Лев"), "август": (24, "Лев", "Дева"),
        "сентябрь": (24, "Дева", "Весы"), "октябрь": (24, "Весы", "Скорпион"),
        "ноябрь": (23, "Скорпион", "Стрелец"), "декабрь": (23, "Стрелец", "Козерог"),
        "январь": (21, "Козерог", "Водолей"), "февраль": (20, "Водолей","Рыбы")}
 

day, month = int(input("Введите день: ")), input("Введите месяц: ")
print(signs[month][2]) if (day >= signs[month][0]) else print(signs[month][1])
