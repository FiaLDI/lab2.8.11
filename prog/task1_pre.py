#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def negative(x):
    print("Отрицательное")

def positive(x):
    print("Положительное")

def test(x):
    if x % 2 == 0:
        positive(x)
    else:
        negative(x)


if __name__ == '__main__':
    x = int(input(""))
    test(x)