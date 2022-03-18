#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Поле first — дробное число; поле second — целое число, показатель степени. Реализовать
метод power() — возведение числа first в степень second. Метод должен правильно
работать при любых допустимых значениях first и second.
"""

class Number:
    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second

    def read(self):
        self.first = float(input("Введите дробное число >> "))
        self.second = int(input("Введите целое число >> "))

    def display(self):
        print(f"Число возведенное в степень", power(self.first, self.second))

def power(first, second):
    # Если число возводимое в степень равно 0
    if first == 0:
        raise ValueError
    else:
        return first ** second


if __name__ == "__main__":
    newNumber = Number(3, 4)
    newNumber.display()
    newNumber.read()
    newNumber.display()
