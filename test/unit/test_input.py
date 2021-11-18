import unittest
import os, sys
# print(os.getcwd())
sys.path.append(os.getcwd())
# print(os.getcwd())

from main.main import *


class TestInput(unittest.TestCase):
    def test_emptyInput(self):
        test_json = ""
        obj = PickLunch()
        with self.assertRaises(FileNotFoundError):
            output = obj.get_ingredients(obj.load_ingredients(test_json))

    def test_emptyJson(self):
        test_json = "/magiclunch/test/unit/test_input1.json"
        obj = PickLunch()
        with self.assertRaises(TypeError):
            output = obj.get_ingredients(obj.load_ingredients(test_json))

    def test_methods(self):
        test_json = "/magiclunch/test/unit/test_input2.json"
        obj = PickLunch()
        output = obj.get_ingredients(obj.load_ingredients(test_json), test=True)
        self.assertIs(type(output), list)
        self.assertEqual(len(output), 16)

    def test_recipe(self):
        test_json = "/magiclunch/test/unit/test_input2.json"
        obj = PickLunch()
        ings = obj.get_ingredients(obj.load_ingredients(test_json), test=True)
        output = obj.match_recipe(ings)
        expected = {
            "Hotdog": ["Hotdog Bun", "Sausage", "Ketchup", "Mustard"],
            "Salad": ["Lettuce", "Tomato", "Cucumber", "Beetroot", "Salad Dressing"],
            "Ham and Cheese Sandwich": ["Ham", "Cheese", "Bread", "Butter"],
        }
        self.assertIs(type(output), dict)
        self.assertEqual(len(output), 3)
        self.assertDictEqual(output, expected)
        self.assertEqual(list(output), list(expected))

    def test_recipe_bestbefore(self):
        test_json = "/magiclunch/test/unit/test_input3.json"
        obj = PickLunch()
        ings = obj.get_ingredients(obj.load_ingredients(test_json), test=True)
        output = obj.match_recipe(ings)
        expected = {
            "Salad": ["Lettuce", "Tomato", "Cucumber", "Beetroot", "Salad Dressing"],
            "Ham and Cheese Sandwich": ["Ham", "Cheese", "Bread", "Butter"],
            "Hotdog": ["Hotdog Bun", "Sausage", "Ketchup", "Mustard"],
        }
        self.assertIs(type(output), dict)
        self.assertEqual(len(output), 3)
        self.assertDictEqual(output, expected)
        self.assertEqual(list(output), list(expected))


if __name__ == "__main__":
    unittest.main()
