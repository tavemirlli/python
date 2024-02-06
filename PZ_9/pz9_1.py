# Вариант 19. Организовать словарь avto, содержащий 3 ключа (марки авто) и списки из 3 моделей в качестве значений.
# Обеспечить отображение вторых моделей по каждому авто, всех моделей словаря.
avto = {
    "Toyota": ["Camry", "Corolla", "RAV4"],
    "BMW": ["3 Series", "5 Series", "X7"],
    "Mercedes": ["S-Class", "E-Class", "GLC"]
}
for brand, models in avto.items():
    print(f"Вторая модель из {brand} это {models[1]}")

for models in avto.values():
    for model in models:
        print(model)