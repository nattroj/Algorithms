#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    l = []

    for ingredient, qty in recipe.items():
        if not ingredients.get(ingredient):
            return 0

        l.append(ingredients[ingredient] // qty)

    minimum = min(l)

    if minimum < 1:
        return 0

    return min(l)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
