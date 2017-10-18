#!usr/bin/env/python
# -*- coding: utf-8 -*-
"""IS211 Assignment Week 6: Refactored"""


class ConversionNotPossible(Exception):

    def __init__(self, message):
        self.message = message


def convert(fromUnit, toUnit, value):

    if fromUnit == "meter":
        if toUnit == "yard":
            x = round(value * 1.0936, 3)
            return x
        elif toUnit == "mile":
            x = round(value / 1609.344, 3)
            return x
        elif toUnit == "meter":
            return value
    elif fromUnit == "yard":
        if toUnit == "meter":
            x = round(value * 0.9144, 0)
            return x
        elif toUnit == "mile":
            x = round(value / 1760.0, 3)
            return x
        elif toUnit == "yard":
            return value

    elif fromUnit == "mile":
        if toUnit == "meter":
            x = round(value * 1609.344, 3)
            return x
        elif toUnit == "yard":
            x = round(value * 1760.0, 3)
            return x
        elif toUnit == "mile":
            return value

    elif fromUnit == "Celsius":
        if toUnit == "Kelvin":
            x = round(value + 273.15, 2)
            return x
        elif toUnit == "Fahrenheit":
            x = round(value * (9.0 / 5.0) + 32, 2)
            return x
        elif toUnit == "Celsius":
            return value

    elif fromUnit == "Kelvin":
        if toUnit == "Fahrenheit":
            x = round((value * (9.0/5.0)) - 459.67, 2)
            return x
        elif toUnit == "Celsius":
            x = round(value - 273.15, 2)
            return x
        elif toUnit == "Kelvin":
            return value
    elif fromUnit == "Fahrenheit":
        if toUnit == "Celsius":
            x = round((value - 32) * (5.0/9.0), 2)
            return x
        elif toUnit == "Kelvin":
            x = round((value + 459.67) * (5.0/9.0), 2)
            return x
        elif toUnit == "Fahrenheit":
            return value
    if fromUnit == "meter" or "yard" or "mile" and toUnit == "Celsius" or "Fahrenheit" or "Kelvin":
        raise ConversionNotPossible('Cannot convert')
