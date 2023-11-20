#!usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils import command
from queue import Empty
import re
import sys

Working = True

def commandExit():
    global Working
    Working = False

def commandAdd(towars):
    name = input("Имя товара: ")
    marketName = input("Имя магазина: ")
    st = int(input("Стоимость товара: "))

    towar = {
        'name':name,
        'marketName':marketName,
        'st':st
    }

    towars.append(towar)

    if len(towars) > 1:
        towars.sort(key=lambda item: item.get('name', ''))
    
    return towars

def commandInfo(towars):
    nameTowar = input('Введите название: ')
    a = False
    for i, item in enumerate(towars):
        for j in towars[i]:
            if towars[i].get(j) == nameTowar:
                print("-"* 10)
                print(f"Имя товара: {towars[i].get('name')}")
                print(f"Имя магазина: {towars[i].get('marketName')}")
                print(f"Стоимость: {towars[i].get('st')}")
                print("-" * 10)
                a = True
    if a == False:
        print(f"Товара с именем {nameTowar} не существует")
  

def checkCommand(command, towars, Working):
    if command == 'exit':
        commandExit()
    elif command == 'add':
        commandAdd(towars)
    elif command == 'info':
        commandInfo(towars)
    
def main():
    towars = []

    while Working:
        command = input(">>> ").lower()
        checkCommand(command, towars, Working)
                       
if __name__ == '__main__':
    main()