#!usr/bin/env/python
# -*- coding: utf-8 -*-
"""IS211 Assignment Week 6: Conversions"""


def convertCelsiustoKelvin(degrees):
    return round(degrees + 273.15, 2)


def convertCelsiustoFahrenheit(degrees):
    return round(degrees * (9.0/5.0) + 32, 2)


def convertFahrenheittoCelsius(degrees):
    return round((degrees - 32) * (5.0/9.0), 2)


def convertFahrenheitoKelvin(degrees):
    return round((degrees + 459.67) * (5.0/9.0), 2)


def convertKelvintoCelsius(degrees):
    return round(degrees - 273.15, 2)


def convertKelvintoFahrenheit(degrees):
    return round((degrees * (9.0/5.0)) - 459.67, 2)


