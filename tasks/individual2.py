#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

"""
Создать класс Vector3D, задаваемый тройкой координат.Обязательно должны быть
реализованы: сложение и вычитание векторов, скалярное произведение векторов,
умножение на скаляр, сравнение векторов, вычисление длины вектора, сравнение длины векторов.
"""

class Vector3D:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split(' ', maxsplit=2)))
        if parts[2] == 0:
            raise ValueError()

        self.x = parts[0]
        self.y = parts[1]
        self.z = parts[2]


    def display(self):
        print(f"Координаты - {self.x}, {self.y}, {self.z}")


    # Сложение
    def add(self, rhs):
        if isinstance(rhs, Vector3D):
            return Vector3D((self.x + rhs.x), (self.y + rhs.y), (self.z + rhs.z))
        else:
            raise ValueError


    # Вычитание
    def sub(self, rhs):
        if isinstance(rhs, Vector3D):
            return Vector3D((rhs.x - self.x), (rhs.y - self.y), (rhs.z - self.z))
        else:
            raise ValueError


    # Скалярное произведение
    def dot(self, rhs):
        if isinstance(rhs, Vector3D):
            return Vector3D((self.x * rhs.x) + (self.y * rhs.y) + (self.z * rhs.z))
        else:
            raise ValueError


    # Сравнение векторов
    def equals(self, rhs):
        if isinstance(rhs, Vector3D):
            return (self.x == rhs.x) and (self.y == rhs.y) and (self.z == rhs.z)
        else:
            return False


    def greater(self, rhs):
        if isinstance(rhs, Vector3D):
            vector1 = (self.x, self.y, self.z)
            vector2 = (rhs.x, rhs.y, rhs.z)
            return vector1 > vector2
        else:
            return False


    def less(self, rhs):
        if isinstance(rhs, Vector3D):
            vector1 = (self.x, self.y, self.z)
            vector2 = (rhs.x, rhs.y, rhs.z)
            return vector1 < vector2
        else:
            return False


    # Вычисление длины векторов
    def length(self, rhs):
        if isinstance(rhs, Vector3D):
            vector1 = math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))
            vector2 = math.sqrt(pow(rhs.x, 2) + pow(rhs.y, 2) + pow(rhs.z, 2))
            return vector1 + vector2
        else:
            raise ValueError


    # Сравнение длины векторов
    def equal(self, rhs):
        if isinstance(rhs, Vector3D):
            vector1 = math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))
            vector2 = math.sqrt(pow(rhs.x, 2) + pow(rhs.y, 2) + pow(rhs.z, 2))
            return vector1 > vector2 or vector1 < vector2
        else:
            raise ValueError


if __name__ == "__main__":
    v1 = Vector3D(4, 1, 2)
    v1.display()

    v2 = Vector3D()
    v2.read("Введите координаты: ")
    v2.display()

    v3 = v2.add(v1)
    v3.display()

    v4 = v2.sub(v1)
    v4.display()

    v5 = v2.dot(v1)
    v5.display()
