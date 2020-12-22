from pathlib import Path
from collections import defaultdict
import sys

TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")

def phase1(data):
    ingredient_counts = defaultdict(int)
    possible_ingredients = defaultdict(lambda: list(ingredient_counts.keys()))
    for ings, allgs in data:
        for ing in ings:
            ingredient_counts[ing] += 1
    
    for ings, allgs in data:
        for allergen in allgs:
            for ing in ingredient_counts:
                if ing not in ings and ing in possible_ingredients[allergen]:
                    possible_ingredients[allergen].remove(ing)
    

    allergens = {}
    has_allergen = []
    for _ in range(len(possible_ingredients)):
        for allergen in possible_ingredients:
            if len(possible_ingredients[allergen]) == 1:
                ingredient = possible_ingredients[allergen].pop()
                allergens[allergen] = ingredient
                has_allergen.append(ingredient)
                for other_allergen in possible_ingredients:
                    if other_allergen != allergen and ingredient in possible_ingredients[other_allergen]:
                        possible_ingredients[other_allergen].remove(ingredient)
    
    total = 0
    for ingredient in ingredient_counts:
        if ingredient not in has_allergen:
            total += ingredient_counts[ingredient]
    
    canonical_list = ""
    for allergen in sorted(allergens):
        canonical_list += allergens[allergen]+","
    return total, canonical_list[:-1]

def load(data):
    result = []
    for line in data:
        ingredients, allergens = line.split(" (contains ")
        ingredients = ingredients.split(" ")
        allergens = allergens[:-1].split(", ")
        result.append([ingredients, allergens])
    return result

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day21_sample" if TEST_MODE else "input/day21").open() as f:
        DATA = load([line.strip() for line in f])

        print('Phase 1: {}\nPhase 2: {}'.format(*phase1(DATA)))