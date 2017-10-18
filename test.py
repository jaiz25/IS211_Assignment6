#!usr/bin/env/python
# -*- coding: utf-8 -*-
"""IS211 Assignment Week 6: Test Cases"""


import unittest
import conversions


class KnownValues(unittest.TestCase):
    knownValues = ((0.0, 273.15, 32.0),
                   (25.2, 298.35, 77.36),
                   (-2.0, 271.15, 28.4),
                   (50.0, 323.15, 122.0),
                   (15.5, 288.65, 59.9))

    def testconvertCelsiustoKelvin(self):

        print "Testing convert Celsius to Kelvin:"

        for number in range(len(self.knownValues)):
            convert = list(self.knownValues)[number][0]
            result = conversions.convertCelsiustoKelvin(convert)
            equal = list(self.knownValues)[number][1]
            self.assertEqual(equal, result)
            print "{}".format(convert) + "°C equals to {}".format(result) + "°K"

    def testconvertCelsiustoFahrenheit(self):

        print "Testing convert Celsius to Fahrenheit."

        for number in range(len(self.knownValues)):
            convert = list(self.knownValues)[number][0]
            result = conversions.convertCelsiustoFahrenheit(convert)
            equal = list(self.knownValues)[number][2]
            self.assertEqual(equal, result)
            print "{}".format(convert) + "°C equals to {}".format(result) + "°F"

    def testconvertKelvintoCelsius(self):

        print "Testing convert Kelvin to Celsius:"

        for number in range(len(self.knownValues)):
            convert = list(self.knownValues)[number][1]
            result = conversions.convertKelvintoCelsius(convert)
            equal = list(self.knownValues)[number][0]
            self.assertEqual(equal, result)
            print "{}".format(convert) + "°K equals to {}".format(result) + "°C"

    def testconvertKelvintoFahrenheit(self):

        print "Testing convert Kelvin to Fahrenheit:"

        for number in range(len(self.knownValues)):
            convert = list(self.knownValues)[number][1]
            result= conversions.convertKelvintoFahrenheit(convert)
            equal = list(self.knownValues)[number][2]
            self.assertEqual(equal, result)
            print "{}".format(convert) + "°K equals to {}".format(result) + "°F"

    def testconvertFahrenheittoCelsius(self):

        print "Testing convert Fahrenheit to Celsius:"

        for number in range(len(self.knownValues)):
            convert = list(self.knownValues)[number][2]
            result = conversions.convertFahrenheittoCelsius(convert)
            equal = list(self.knownValues)[number][0]
            self.assertEqual(equal, result)
            print "{}".format(convert) + "°F equals to {}".format(result) + "°C"

    def testconvertFahrenheittoKelvin(self):

        print "Testing convert Fahrenheit to Kelvin:"

        for number in range(len(self.knownValues)):
            convert = list(self.knownValues)[number][2]
            result = conversions.convertFahrenheitoKelvin(convert)
            equal = list(self.knownValues)[number][1]
            self.assertEqual(equal, result)
            print "{}".format(convert) + "°F equals to {}".format(result) + "°K"


if __name__ == "__main__":
    unittest.main()


