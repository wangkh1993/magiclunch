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

        return ingredients

    def get_ingredients(self, ingredients):
        if ingredients and ingredients.get('ingredients'):
            in_ingres = []
            for ing in ingredients.get('ingredients'):
                if self.check_date(ing.get('use-by')):
                    if self.check_date(ing.get('best-before')):
                        in_ingres.append({'ingredient': ing.get('title'), 'weight': 1})
                    else:
                        in_ingres.append({'ingredient': ing.get('title'), 'weight': 100})
                else:
                    continue
            return in_ingres
        else:
            raise(TypeError('Input ingredients JSON is an empty file! Please verify'))

    def match_recipe(self, in_ingredients):
        out_recipes = []
        ings_candidates = [i.get('ingredient') for i in in_ingredients]

        ings_bestbefore = [i.get('ingredient') for i in in_ingredients if i.get('weight') == 100]
        for recipe, ingredients in self.new_recipes.items():
            if all(ing in ings_candidates for ing in ingredients):
                if any(ing in ings_bestbefore for ing in ingredients):
                    out_recipes.append(recipe)
                else:
                    out_recipes.insert(0, recipe)
        output = {}
        for out_recipe in out_recipes:
            output[out_recipe] = self.new_recipes.get(out_recipe)

        return output


if __name__ == '__main__':
    obj = PickLunch()
    # print(obj.new_recipes)
    user_input = input('Please provide your ingredients JSON file\n')
    # ing_json = "../data/ingredients.json"
    ings = obj.get_ingredients(obj.load_ingredients(user_input))
    # print(ings)

    choice = obj.match_recipe(ings)
    print(choice)