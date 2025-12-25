#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # !/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import sys
    from datetime import date

    if __name__ == '__main__':
        school = {}

        while True:
            command = input(">>> ").lower()

            if command == "exit":
                break

            elif command == "add":
                school_class = input("Введите цифру и букву класса без пробела: ")

                worker = {
                    'name': name,
                    'post': post,
                    'year': year,
                }

                workers.append(worker)
                if len(workers) > 1:
                    workers.sort(key=lambda item: item.get('name', ''))

            elif command == "list":
                line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                    '-' * 4,
                    '-' * 30,
                    '-' * 20,
                    '-' * 8
                )
                print(line)
                print(
                    '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                        "№",
                        "Ф.И.О.",
                        "Должность",
                        "Год"
                    )
                )
                print(line)

                for idx, worker in enumerate(workers, 1):
                    print(
                        '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                            idx,
                            worker.get('name', ''),
                            worker.get('post', ''),
                            worker.get('year', '')
                        )
                    )

                print(line)

            elif command.startswith('select'):
                today = date.today()
                parts = command.split(' ', maxsplit=1)
                period = int(parts[1])

                count = 0
                for worker in workers:
                    if today.year - worker.get('year', today.year) >= period:
                        count += 1
                        print(
                            '{:>4}: {}'.format(count, worker.get('name', ''))
                        )

                if count == 0:
                    print("Работники с заднным стажем не найдены. ")

            elif command == 'help':
                print("Список команд:\n")
                print("add - добавить работника;\n")
                print("list - вывести список работников;\n")
                print("select <стаж> - запросить работников со стажем;\n")
                print("help - отобразить справку;\n")
                print("exit - завершить работу с программой;\n")

            else:
                print(f"Неизвестная команда {command}", file=sys.stderr)


