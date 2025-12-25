#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import date


if __name__ == '__main__':
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {'b', 'k', 'n', 'o', 'q'}
    b = {'a', 'b', 'k', 'u'}
    c = {'o', 'p'}
    d = {'a', 'm', 'n', 'y', 'z'}

    x = (a.union(b)).intersection(d)
    y = ((u - a).intersection(d)).union(c - b)

    print(f"x = {x}. y = {y}")