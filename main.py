import os.path
import datetime
import json


def generator_loger(path):
    person = int(input('Сколько персон будет подчевать? '))
    dish_quantity = int(input('Введите количество блюд '))
    now = datetime.datetime.now()

    def loger(shop):
        def new_shop():
            nonlocal person, dish_quantity
            params = shop(person, dish_quantity)
            time = {'Время зпуска функции': str(now)}
            name = {'Имя функции': str(shop)}
            param = {'Параметры функции': [{
                'Количество персон': str(person),
                'количество блюд': str(dish_quantity)
            }]}
            answer = {'Функция вернула': params}
            log = [time, name, param, answer]
            with open(f'{path}', mode='w', encoding='utf8') as f:
                json.dump(log, f, ensure_ascii=False, indent=2)
            return params
        return new_shop
    return loger


workdir = os.path.dirname(__file__)
cook_book = {}


if __name__== '__main__':
    @generator_loger(f'{workdir}/log.json')
    def shop(person, dish_quantity):
        dishes = []
        for i in range(dish_quantity):
            dishes.append(cook_book.get(input('какое блюдо будете готовить?')))
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
                    ingridient = dict(
                        [('ingridient_name', ing_list[0]), ('quantity', ing_list[1]), ('measure', ing_list[2])])
                    recept.append(ingridient)
                cook_book[line.strip()] = recept
                f.readline()
            return cook_book

    read()
    shop()
