import json
from datetime import datetime
import os

absolute_path = os.path.dirname(os.path.abspath(__file__))


class PickLunch(object):
    """
    A class to return recipe options with provided JSON ingredients file
    """

    def __init__(self):
        with open(absolute_path + "/../data/recipes.json") as f:
            self.recipes = json.loads(f.read())
        self.new_recipes = self.__convert_recipe()

    def __convert_recipe(self):
        """
        Convert input ingredients JSON to new dict with key being the recipe and value being ingredients
        :return: dict
        """
        new_recipes = {}
        for recipe in self.recipes["recipes"]:
            new_recipes[recipe.get("title")] = recipe.get("ingredients")

        return new_recipes

    def check_date(self, datein, test=False, default_date="2021-11-18"):
        """
        Compare input date against current date to validate use-by/best-before date, if test flag is true, use default date instead
        :return: bool, True/False
        """
        if test:
            today = datetime.strptime(default_date, "%Y-%m-%d")
        else:
            today = datetime.today()
        datein_t = datetime.strptime(datein, "%Y-%m-%d")
        if today <= datein_t:
            return True
        else:
            return False

    def load_ingredients(self, json_file):
        """
        Load input JSON file
        :param json_file: JSON file
        :return: dict
        """
        with open(json_file) as f:
            ingredients = json.loads(f.read())
        return ingredients

    def get_ingredients(self, ingredients, test=False):
        """
        Parse input ingredients, skip ingredients with past use-by datge, assign default 1 as weight, if best-before is past, assign 100
        :param ingredients: dict
        :param test: bool
        :return: list of dict
        """
        if ingredients and ingredients.get("ingredients"):
            in_ingres = []
            for ing in ingredients.get("ingredients"):
                if self.check_date(ing.get("use-by"), test):
                    if self.check_date(ing.get("best-before"), test):
                        in_ingres.append({"ingredient": ing.get("title"), "weight": 1})
                    else:
                        in_ingres.append(
                            {"ingredient": ing.get("title"), "weight": 100}
                        )
                else:
                    continue
            return in_ingres
        else:
            # in case input JSON is an empty file, raise TypeError
            raise (TypeError("Input ingredients JSON is an empty file! Please verify"))

    def match_recipe(self, in_ingredients):
        """
        Check input ingredients against recipe required ingredients, output matched recipes as JSON, if ingredient has a past best-before date, push recipe to the bottom
        :param in_ingredients: dict
        :return: dict
        """
        out_recipes = []

        # all the valid ingredients
        ings_candidates = [i.get("ingredient") for i in in_ingredients]

        # all the valid ingredients has a past best-before date
        ings_bestbefore = [
            i.get("ingredient") for i in in_ingredients if i.get("weight") == 100
        ]
        for recipe, ingredients in self.new_recipes.items():
            if all(ing in ings_candidates for ing in ingredients):
                if any(ing in ings_bestbefore for ing in ingredients):
                    out_recipes.append(recipe)
                else:
                    # use insert to push best-before recipe to the left
                    out_recipes.insert(0, recipe)
        output = {}
        for out_recipe in out_recipes:
            output[out_recipe] = self.new_recipes.get(out_recipe)

        return output


if __name__ == "__main__":
    obj = PickLunch()
    while 1:
        user_input = input("Please provide your ingredients JSON file\n")
        if not user_input:
            raise (TypeError("Input must NOT be empty"))
        # ing_json = "../data/ingredients.json"
        ings = obj.get_ingredients(obj.load_ingredients(user_input))
        choice = obj.match_recipe(ings)
        print(choice)

