#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import date


if __name__ == '__main__':
    people = []

    while True:
        command = input(">>> ").lower()

        if command == "exit":
            break

        elif command == "add":
            name = input("Фамилия и имя: ")
            phone = input("Номер телефона: ")
            year, month, day = map(int, input("Дата рождения (гггг мм дд): ").split())
            birthday = date(year, month, day)

            person = {
                'name': name,
                'phone': phone,
                'birthday': birthday
            }

            people.append(person)
            if len(people) > 1:
                people.sort(key=lambda item: item.get('name', ''))

        elif command == "list":
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "№",
                    "Фамилия Имя",
                    "Номер телефона",
                    "Дата рождения"
                )
            )
            print(line)

            for idx, person in enumerate(people, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                        idx,
                        person.get('name', ''),
                        person.get('phone', ''),
                        str(person.get('birthday', ''))
                    )
                )

            print(line)

        elif command.startswith('select'):
            parts = command.split(' ', maxsplit=1)
            birth_month = int(parts[1])

            count = 0
            for person in people:
                if person['birthday'].month == birth_month:
                    count += 1
                    print(person.get('name', ''))
            if count == 0:
                print("Нет человека с днем рождения в этом месяце")


        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить работника;\n")
            print("list - вывести список работников;\n")
            print("select <месяц> - вывести имена людей, у которых день рождение в этом месяце;\n")
            print("help - отобразить справку;\n")
            print("exit - завершить работу с программой;\n")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)