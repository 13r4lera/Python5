#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    school = {}

    while True:
        command = input(">>> ").lower()

        if command == "exit":
            break

        elif command == "add":

            name = input("Введите цифру и букву класса без пробела: ")
            amount = int(input("Введите количество учеников: "))
            school[name] = amount

            if len(school) > 1:
                school = dict(sorted(school.items()))

        elif command == "list":
            line = '+-{}-+-{}-+'.format(
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^20} | {:^20} |'.format(
                    "Название класса",
                    "Количество человек"
                )
            )
            print(line)

            for name, amount in school.items():
                print('| {:^20} | {:^20} |'.format(name, amount))

            print(line)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить класс;\n")
            print("list - вывести список классов;\n")
            print("change класс количество - изменить количество учеников в классе;\n")
            print("delete класс - расформировать класс;\n")
            print("help - отобразить справку;\n")
            print("exit - завершить работу с программой;\n")

        elif command.startswith("change"):
            parts = command.split(' ', maxsplit=2)
            class_name = parts[1]
            class_amount = int(parts[2])

            if class_name in school:
                school[class_name] = class_amount
            else:
                print("Такого класса нет в школе!", file=sys.stderr)

        elif command.startswith("delete"):
            parts = command.split(' ', maxsplit=1)
            class_name = parts[1]
            if class_name in school:
                school.pop(class_name)

        elif command == 'total':
            total_amount = sum(school.values())
            print(f"Общее количество учеников: {total_amount}")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)