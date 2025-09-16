"""1. Реализовать программу для подсчёта индекса массы
тела человека. Пользователь вводит рост и вес с клавиатуры.
На выходе – ИМТ и пояснение к нему в зависимости от
попадания в тот или иной диапазон. Использовать обработку
исключений."""
try:
    weight = float(input("Введите вес в кг: "))
    height = float(input("Введите рост в м: "))
    imt= weight / (height ** 2)

    if imt< 18.5:
        category = "Недостаточный вес"
    elif imt < 25:
        category = "Нормальный вес"
    elif  imt < 30:
        category = "Избыточный вес"
    else:
        category = "Ожирение"

    print(f"Ваш ИМТ: {imt}")
    print(f"Результат: {category}")

except ValueError:
    print("Ошибка! Вводите только числа")
except ZeroDivisionError:
    print("Ошибка! Рост не может быть нулем")
except:
    print("УПС! Ошибка")