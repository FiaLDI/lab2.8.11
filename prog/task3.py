#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def proizv():
    pr = 1

    while True:
        x = int(input())
        if x == 0:
            break
        pr *= x
    
    return pr

def main():
    print(proizv())

if __name__ == "__main__" :
    main()