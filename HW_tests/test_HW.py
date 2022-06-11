from sidorov5 import *
import unittest


class TestHomework(unittest.TestCase):

    def setUp(self) -> None:
        self.name = validate_name
        self.age = validate_age
        self.passport = change_passport
        self.clean = clean
        self.main = main

    def test_name_positive(self):
        self.assertEqual(self.name(""), "Error: empty name!")
        self.assertEqual(self.name("Jack Kusto Kusto"), "Error: name can't contain more than one space!")
        self.assertEqual(self.name(" "), "Error: the name must contain at least 3 characters!")

    def test_name_negative(self):
        self.assertNotEqual(self.name("Aliaksei"), "Hello, Aliaksei.")
        self.assertNotEqual(self.name("123123123"), "Hello, 123123123")
        self.assertNotEqual(self.name("Jack If"), "Hello, Jack If.")

    def test_age_positive(self):
        self.assertEqual(self.age(-2), "Error: enter the correct age!")
        self.assertEqual(self.age(5), "Error: you need to grow up to 14 years old!")
        self.assertEqual(self.age(20), "")

    def test_age_negative(self):
        self.assertNotEqual(self.age(2), "")
        self.assertNotEqual(self.age(15), "You are 15 years old.")
        self.assertNotEqual(self.age(25), "You are 25 years old.")

    def test_clean_positive(self):
        self.assertEqual(self.clean("alex         "), "alex")
        self.assertEqual(self.clean("         alex"), "alex")
        self.assertEqual(self.clean("   alex    "), "alex")

    def test_clean_negative(self):
        self.assertNotEqual(self.clean("alex"), "  alex")
        self.assertNotEqual(self.clean("alex   "), "alex   ")
        self.assertNotEqual(self.clean("  alex  "), "  alex  ")

    def test_main_positive(self):
        self.assertEqual(self.main("alex", 27), "Hello, alex. You are 27 years old. ")
        self.assertEqual(self.main("Aliaksei", 25),
                         "Hello, Aliaksei. You are 25 years old. Don't forget to replace your passport after 25 years.")
        self.assertEqual(self.main("Jack If", 15), "Hello, Jack If. You are 15 years old. ")

    def test_main_negative(self):
        self.assertNotEqual(self.main("al", 30), "Hello, al. You are 30 years old. ")
        self.assertNotEqual(self.main("alex", 10), "Hello, alex. You are 10 years old. ")
        self.assertNotEqual(self.main("Jack If Kusto", -5), "Hello, Jack if Kusto, You are -5 years old. ")
