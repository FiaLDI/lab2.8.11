#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    x = input()

    return x

def test_input(x):
    return x.isdigit()

def str_to_int(x):
    return int(x)

def print_int(x):
    print(x)

def main():
    x = get_input()
    if test_input(x):
        y = str_to_int(x)
        print_int(y)

if __name__ == "__main__":
    main()