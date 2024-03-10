# Задание № 1
cook_book = {}
with open('test.txt', 'r', encoding='utf-8') as f:
    for row in f:
        dishes = row.strip()
        i = f.readline()
        # i = int(line_i)
        tmp = []
        for _ in range(int(i)):
            dish_list = f.readline().strip().split(' | ')
            ingredient_name, quantity, measure = dish_list
            tmp.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure, })
        f.readline()
        cook_book[dishes] = tmp

print(cook_book)
# Задание № 2
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count
            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
            else:
                shop_list[ingredient_name]['quantity'] += quantity
    return shop_list

result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(result)
