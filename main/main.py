import json
from datetime import datetime


class PickLunch(object):
    def __init__(self):
        with open("../data/recipes.json") as f:
            self.recipes = json.loads(f.read())
        self.new_recipes = self.__convert_recipe()

    def __convert_recipe(self):
        new_recipes = {}
        for recipe in self.recipes['recipes']:
            new_recipes[recipe.get('title')] = recipe.get('ingredients')

        return new_recipes

    def check_date(self, datein):
        """
        check uer-by date against current date
        :return: True/False
        """
        today = datetime.today()
        datein_t = datetime.strptime(datein, '%Y-%m-%d')
        if today <= datein_t:
            return True
        else:
            return False

    def load_ingredients(self, json_file):
        with open(json_file) as f:
            ingredients = json.loads(f.read())
        # Handle empty file here

        return ingredients.get('ingredients')

    def get_ingredients(self, ingredients):
        in_ingres = []
        for ing in ingredients:
            if self.check_date(ing.get('use-by')):
                if self.check_date(ing.get('best-before')):
                    in_ingres.append({ing.get('title'): 1})
                else:
                    in_ingres.append({ing.get('title'): 100})
            else:
                continue
        return in_ingres



if __name__ == '__main__':
    obj = PickLunch()
    print(obj.new_recipes)
    ing_json = "../data/ingredients.json"
    ings = obj.get_ingredients(obj.load_ingredients(ing_json))
    for i in ings:
        print(i.keys())