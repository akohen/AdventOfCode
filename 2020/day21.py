from pathlib import Path
from collections import defaultdict
import sys

TEST_MODE = bool(len(sys.argv) > 1 and sys.argv[1] == "test")

def solve(data):
    ingredient_counts = defaultdict(int)
    possible_ingredients = defaultdict(lambda: set(ingredient_counts.keys()))
    for ings, allgs in data:
        for ing in ings:
            ingredient_counts[ing] += 1
    
    for ings, allgs in data:
        for allergen in allgs:
            possible_ingredients[allergen] &= set(ings)
    

    allergens = {}
    while any(possible_ingredients.values()):
        allergen, ingredient = next((a, possible_ingredients[a].pop()) for a in possible_ingredients if len(possible_ingredients[a]) == 1)
        allergens[allergen] = ingredient
        for other_allergen in possible_ingredients:
            possible_ingredients[other_allergen].discard(ingredient)

    total = sum([ingredient_counts[ingredient] for ingredient in ingredient_counts if ingredient not in allergens.values()])
    canonical_list = ",".join([allergens[allergen] for allergen in sorted(allergens)])
    return total, canonical_list

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day21_sample" if TEST_MODE else "input/day21").open() as f:
        DATA = [[a[0].split(" "), a[1][:-1].split(", ")] for line in f if (a := line.strip().split(" (contains "))]

        print('Phase 1: {}\nPhase 2: {}'.format(*solve(DATA)))