#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    '''
    Ввод с клавиатуры.
    '''
    x = input()

    return x


def test_input(x):
    '''
    Проверка на число.
    '''
    return x.isdigit()


def str_to_int(x):
    '''
    Перевод в число.
    '''
    return int(x)


def print_int(x):
    '''
    Вывод.
    '''
    print(x)


def main():
    '''
    Главная функция программы.
    '''
    x = get_input()
    if test_input(x):
        y = str_to_int(x)
        print_int(y)


if __name__ == "__main__":
    main()