#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    text1 = input("Введите первую строку:  ")
    text2 = input("Введите вторую строку:  ")

    common = set(text1).intersection(text2)
    print(f"Общие символы в двух строках: {common}")