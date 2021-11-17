
from datetime import datetime


class PickLunch(object):
    def __init__(self):
        import json
        with open("../data/recipes.json") as f:
            self.recipes = json.loads(f.read())
        self.new_recipes = self.__convert_recipe()

    def __convert_recipe(self):
        new_recipes = {}
        for recipe in self.recipes['recipes']:
            new_recipes[recipe.get('title')] = recipe.get('ingredients')

        return new_recipes

    def check_useby(self):
        """
        check uer-by date against current date
        :return: True/False
        """
        return None

    def get_receipe(self):

        return None

    def match_receipe(self):

        return None


if __name__ == '__main__':
    obj = PickLunch()
    print(obj.new_recipes)