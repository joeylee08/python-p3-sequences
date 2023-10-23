#!/usr/bin/env python3

def print_fibonacci(length):
    result = []
    a = 0
    b = 1
    c = 1
    while (len(result) < length):
        result.append(a)
        a = b
        b = c
        c = a + b
    print(result)

print_fibonacci(10)