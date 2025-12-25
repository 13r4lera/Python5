#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s = input("Введите строку:  ").lower()
    vowels = {'ё', 'у', 'е', 'э', 'о', 'а', 'ы', 'я', 'и', 'ю'}

    count = 0
    for vowel in vowels:
        count += s.count(vowel)

    print(f"В написанной строке {count} гласных.")