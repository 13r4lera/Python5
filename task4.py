#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    reversed_numbers = {}

    for k, v in numbers.items():
        reversed_numbers[v] = k

    print(reversed_numbers)