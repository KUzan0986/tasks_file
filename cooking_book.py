from pprint import pprint

cook_book = {}
list_to_buy = {}
counter = 0

with open("recipes.txt", encoding="utf-8") as file:
    count_lines = len([0 for _ in file])


with open("recipes.txt", encoding="utf-8") as file:
    while True:
        stri_dish = file.readline().strip()
        counter += 1
        cook_book[stri_dish] = []
        try:
            number = int(file.readline().strip())
        except ValueError:
            break
        for ingridients in range(number):
            stri = file.readline().strip()
            spliter = stri.split(" | ")
            cook_book[stri_dish] += [{'ingredient_name': spliter[0], 'quantity': int(spliter[1]), 'measure': spliter[2]}]
        file.readline()


def ingr_to_buy(list_dish, persons):
    value_dict = {}
    for dish in list_dish:
        ingr = cook_book[dish]
        for ingr_to_dish in ingr:
            if value_dict.get(ingr_to_dish['ingredient_name']) is None:
                value_dict[ingr_to_dish['ingredient_name']] = {'measure': ingr_to_dish['measure'], 'quantity': int(ingr_to_dish['quantity']) * persons}
            else:
                value_dict[ingr_to_dish['ingredient_name']]['quantity'] += int(ingr_to_dish['quantity']) * persons
    return value_dict

pprint(ingr_to_buy(["Омлет", "Фахитос"], 5))
pprint(cook_book)