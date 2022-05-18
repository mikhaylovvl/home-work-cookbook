with open("recipe.txt", encoding='UTF8') as recipe_book:
    cook_book = {}
    for line in recipe_book:
        my_list = []
        if line.strip().isdigit():
            for idx in range(int(line)):
                arr = recipe_book.readline().strip().split('|')
                my_list.append({'ingredient_name': arr[0], 'quantity': arr[1], 'measure': arr[2]})
            cook_book[key_name] = my_list
        else:
            key_name = line.strip()

print(f'cook_book = {cook_book}')


def get_shop_list_by_dishes(dishes, person_count):
    total_ingredients = {}
    for id_dishes in dishes:
        if id_dishes in cook_book.keys():
            temp_arr = cook_book[id_dishes]
            for id_cook_book in temp_arr:
                total = int(id_cook_book['quantity']) * person_count
                total_ingredients[id_cook_book['ingredient_name']] = {'measure': id_cook_book['measure'],
                                                                      'quantity': total}
    print(total_ingredients)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
