#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pi

def cylinder(r, h):
    """
    Вычисляет площадь цилиндра.
    """
    def circle(r) -> int:
        return pi * r * r
    x = input("Получить площадь боковой поверхности? Да - Нет: ")
    if x == "Да" or x == "да":
        return 2* pi * r * h
    
    return 2 * circle(r) + 2 * pi * r * h


def main():
    """
    Главная функция программы.
    """
    print(cylinder(3, 4))


if __name__ == '__main__':
    main()