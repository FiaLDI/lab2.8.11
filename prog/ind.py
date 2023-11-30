#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def get_product():
    """
    Запросить данные о продукте.
    """
    name_of_product = input("Имя товара: ")
    name_of_market = input("Имя магазина: ")
    value = int(input("Стоимость товара: "))

    return {
        'name_of_product':name_of_product,
        'name_of_market':name_of_market,
        'value':value
    }

      
def display_products(workers):
    """
    Отобразить список работников.
    """
    if workers:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 10
        )
        print(line)
        print(
                '| {:^4} | {:^30} | {:^20} | {:^10} |'.format(
                    "№",
                    "Название продукта",
                    "Имя магазина",
                    "Стоимость"
            )
        )
        print(line)
        for idx, worker in enumerate(workers, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>10} |'.format(
                    idx,
                    worker.get('name_of_product', ''),
                    worker.get('name_of_market', ''),
                    worker.get('value', 0)
                )
            )
        print(line)
       
    else:
        print("Список работников пуст.")
       
       
def select_products(products, find_name):
    """
    Выбрать продукт с заданным именем.
    """
    result = []
    for product in products:
        if product.get('name_of_product') == find_name:
            result.append(product)

    return result


def main():
    """
    Главная функция программы.
    """
    products = []
    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            product = get_product()
            products.append(product)
            if len(products) > 1:
                products.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            display_products(products)

        elif command.startswith('info '):
            parts = command.split(' ', maxsplit=1)
            find_name = parts[1]
            selected = select_products(products, find_name)
            display_products(selected)

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()