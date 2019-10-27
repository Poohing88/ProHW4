# читаем файл
# создаем общий словарь
# создаем список рецептуры
# в списке делаем словарь ингридиента
# добавляем словарь в список рецептуры


cook_book = {}


def read():
    ingridient = {'ingridient_name': '', 'quantity': '', 'measure': ''}
    ing_list = []
    with open('recipes.txt') as f:
        for line in f:
            x = int(f.readline())
            counter = 0
            recept = []
            while counter < x:
                counter += 1
                ing_list = f.readline().strip().split(' | ')
                ingridient = dict([('ingridient_name', ing_list[0]), ('quantity', ing_list[1]), ('measure', ing_list[2])])
                recept.append(ingridient)
            cook_book[line.strip()] = recept
            f.readline()
        return cook_book

#
# person = int(input('Сколько персон будет подчевать? '))
# dish_quantity = int(input('Введите количество блюд '))


def shop(person, dish_quantity):
    dishes = []
    for i in range(dish_quantity):
        dishes.append(cook_book.get(input('Какое блюдо будете готовить?')))
    shop_list = {}
    counter = 0
    while counter < dish_quantity:
        for lists in dishes[counter]:
            dish = lists['ingridient_name']
            mass = int(lists['quantity']) * person
            unit_of_measure = lists['measure']
            if dish in shop_list.keys():
                shop_list[dish]['quantity'] = int(shop_list[dish]['quantity'] + mass)
            else:
                list = {'quantity': mass, 'measure': unit_of_measure}
                shop_list.setdefault(dish)
                shop_list[dish] = list
        counter += 1
    print(shop_list)
    return shop_list


read()
