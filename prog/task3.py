#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def work_up_to():
    """
    Считывает и перемножает числа.
    """
    work = 1

    while True:
        x = int(input())
        if x == 0:
            break
        work *= x
    
    return work


def main():
    """
    Главная функция программы.
    """
    print(work_up_to())


if __name__ == "__main__" :
    main()