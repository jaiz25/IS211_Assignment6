#!usr/bin/env/python
# -*- coding: utf-8 -*-
"""IS211 Assignment Week 6: Refactored test"""


import unittest
import conversions_refactored


class KnownValues(unittest.TestCase):
    knownValues = ((0.0, 273.15, 32.0),
                   (25.2, 298.35, 77.36),
                   (-2.0, 271.15, 28.4),
                   (50.0, 323.15, 122.0),
                   (15.5, 288.65, 59.9))

    def testconvert(self):

        print "Testing Celsius to Kelvin conversion."
        for item in range(len(self.knownValues)):
            knownValueslist = list(self.knownValues)[item][0]
            result_1 = conversions_refactored.convert("Celsius", "Kelvin", value=knownValueslist)
            equal = list(self.knownValues)[item][1]
            self.assertEqual(result_1, equal)
            print "{}".format(knownValueslist) + "°C equals to {}".format(result_1) + "°K"

        print "Testing Celsius to Fahrenheit conversion."
        for item in range(len(self.knownValues)):
            knownValueslist = list(self.knownValues)[item][0]
            result_2 = conversions_refactored.convert("Celsius", "Fahrenheit", value=knownValueslist)
            equal = list(self.knownValues)[item][2]
            self.assertEqual(result_2, equal)
            print "{}".format(knownValueslist) + "°C equals to {}".format(result_2) + "°F"

        print "Testing Kelvin to Fahrenheit conversion."
        for item in range(len(self.knownValues)):
            knownValueslist = list(self.knownValues)[item][1]
            result_3 = conversions_refactored.convert("Kelvin", "Fahrenheit", value=knownValueslist)
            equal = list(self.knownValues)[item][2]
            self.assertEqual(result_3, equal)
            print "{}".format(knownValueslist) + "°K equals to {}".format(result_3) + "°F"

        print "Testing Kelvin to Celsius conversion."
        for item in range(len(self.knownValues)):
            knownValueslist = list(self.knownValues)[item][1]
            result_4 = conversions_refactored.convert("Kelvin", "Celsius", value=knownValueslist)
            equal = list(self.knownValues)[item][0]
            self.assertEqual(result_4, equal)
            print "{}".format(knownValueslist) + "°K equals to {}".format(result_4) + "°C"

        print "Testing Fahrenheit to Celsius conversion."
        for item in range(len(self.knownValues)):
            knownValueslist = list(self.knownValues)[item][2]
            result_5 = conversions_refactored.convert("Fahrenheit", "Celsius", value=knownValueslist)
            equal = list(self.knownValues)[item][0]
            self.assertEqual(result_5, equal)
            print "{}".format(knownValueslist) + "°F equals to {}".format(result_5) + "°C"

        print "Testing Fahrenheit to Kelvin conversion."
        for item in range(len(self.knownValues)):
            knownValueslist = list(self.knownValues)[item][2]
            result_6 = conversions_refactored.convert("Fahrenheit", "Kelvin", value=knownValueslist)
            equal = list(self.knownValues)[item][1]
            self.assertEqual(result_6, equal)
            print "{}".format(knownValueslist) + "°F equals to {}".format(result_6) + "°K"


class KnownValues2(unittest.TestCase):
    knownvalues = ((1000, 1093.6, 0.621),
                   (2000, 2187.2, 1.243),
                   (3000, 3280.8, 1.864),
                   (10000, 10936.0, 6.214),
                   (5500, 6014.8, 3.418))

    def testdistanceconversion(self):

        print "Testing meter to yard conversion."
        for item in range(len(self.knownvalues)):
            knownvaluelist = list(self.knownvalues)[item][0]
            result = conversions_refactored.convert("meter", "yard", value=knownvaluelist)
            equal = list(self.knownvalues)[item][1]
            self.assertEqual(result, equal)
            print "{}".format(knownvaluelist) + " m equals to {}".format(result) + " yd."

        print "Testing meter to mile conversion."
        for item in range(len(self.knownvalues)):
            knownvaluelist = list(self.knownvalues)[item][0]
            result = conversions_refactored.convert("meter", "mile", value=knownvaluelist)
            equal = list(self.knownvalues)[item][2]
            self.assertEqual(result, equal)
            print "{}".format(knownvaluelist) + " m equals to {}".format(result) + " mi."

        print "Testing yard to meter conversion."
        for item in range(len(self.knownvalues)):
            knownvaluelist = list(self.knownvalues)[item][1]
            result = conversions_refactored.convert("yard", "meter", value=knownvaluelist)
            equal = list(self.knownvalues)[item][0]
            self.assertEqual(result, equal)
            print "{}".format(knownvaluelist) + " yd equals to {}".format(result) + " m."

        print "Testing yard to mile conversion."
        for item in range(len(self.knownvalues)):
            knownvaluelist = list(self.knownvalues)[item][1]
            result = conversions_refactored.convert("yard", "mile", value=knownvaluelist)
            equal = list(self.knownvalues)[item][2]
            self.assertEqual(result, equal)
            print "{}".format(knownvaluelist) + " yd equals to {}".format(result) + " mi."

        print "Testing mile to meter conversion."
        for item in range(len(self.knownvalues)):
            knownvaluelist = list(self.knownvalues)[item][2]
            result = conversions_refactored.convert("mile", "meter", value=knownvaluelist)
            equal = list(self.knownvalues)[item][0]
            self.assertEqual(result, equal)
            print "{}".format(knownvaluelist) + " mi equals to {}".format(result) + " m."

        print "Testing mile to yard conversion."
        for item in range(len(self.knownvalues)):
            knownvaluelist = list(self.knownvalues)[item][2]
            result = conversions_refactored.convert("mile", "yard", value=knownvaluelist)
            equal = list(self.knownvalues)[item][1]
            self.assertEqual(result, equal)
            print "{}".format(knownvaluelist) + " mi equals to {}".format(result) + " yd."


class IncompatibleUnitInput(unittest.TestCase):
    def distance_to_temperature(self):

        for distance in ('mile', 'meter', 'yard'):
            self.assertRaises(conversions_refactored.ConversionNotPossible, conversions_refactored.convert
            (fromUnit=distance, toUnit='Celsius'))
            self.assertRaises(conversions_refactored.ConversionNotPossible, conversions_refactored.convert
            (fromUnit=distance, toUnit='Fahrenheit'))
            self.assertRaises(conversions_refactored.ConversionNotPossible, conversions_refactored.convert
            (fromUnit=distance, toUnit='Kelvin'))


    def temperature_to_distance(self):

        for temperature in ('Kelvin', 'Celsius', 'Fahrenheit'):
            self.assertRaises(conversions_refactored.ConversionNotPossible, conversions_refactored.convert
            (fromUnit=temperature, toUnit='meter'))
            self.assertRaises(conversions_refactored.ConversionNotPossible, conversions_refactored.convert
            (fromUnit=temperature, toUnit='mile'))
            self.assertRaises(conversions_refactored.ConversionNotPossible, conversions_refactored.convert
            (fromUnit=temperature, toUnit='yard'))


class SanityCheck(unittest.TestCase):
    def testSanity(self):

        for integer in range(0, 10000):
            from_mile = conversions_refactored.convert('mile', 'mile', integer)
            result = conversions_refactored.convert('mile', 'mile', from_mile)
            self.assertEqual(integer, result)

        for integer in range(0, 10000):
            from_mile = conversions_refactored.convert('meter', 'meter', integer)
            result = conversions_refactored.convert('meter', 'meter', from_mile)
            self.assertEqual(integer, result)

        for integer in range(0, 10000):
            from_mile = conversions_refactored.convert('yard', 'yard', integer)
            result = conversions_refactored.convert('yard', 'yard', from_mile)
            self.assertEqual(integer, result)

        for integer in range(0, 10000):
            from_mile = conversions_refactored.convert('Celsius', 'Celsius', integer)
            result = conversions_refactored.convert('Celsius', 'Celsius', from_mile)
            self.assertEqual(integer, result)

        for integer in range(0, 10000):
            from_mile = conversions_refactored.convert('Kelvin', 'Kelvin', integer)
            result = conversions_refactored.convert('Kelvin', 'Kelvin', from_mile)
            self.assertEqual(integer, result)

        for integer in range(0, 10000):
            from_mile = conversions_refactored.convert('Fahrenheit', 'Fahrenheit', integer)
            result = conversions_refactored.convert('Fahrenheit', 'Fahrenheit', from_mile)
            self.assertEqual(integer, result)


if __name__ == "__main__":
    unittest.main()
