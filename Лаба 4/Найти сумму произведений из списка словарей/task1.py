import json

def task() -> float:
    total_product = 0.0

    # Чтение JSON файла
    with open("input.json", "r") as json_file:
        data = json.load(json_file)

    # Перебор словарей
    for item in data:
        score = item.get("score", 0)

        weight = item.get("weight", 1)  # Получаем значение "weight", по умолчанию 1
        product = score * weight  # Вычисляем произведение
        total_product += product

    return round(total_product, 3)

print(task())