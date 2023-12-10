#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def negative(x):
    """
    Вывод информации о четности числа
    """
    print("Отрицательное")


def positive(x):
    """
    Вывод информации о четности числа
    """
    print("Положительное")


def test(x):
    """
    Проверка числа на четность
    """
    if x > 0:
        positive(x)
    else:
        negative(x)


def main():
    """
    Главная функция программы.
    """
    x = int(input(""))
    test(x)


if __name__ == '__main__':
    main()