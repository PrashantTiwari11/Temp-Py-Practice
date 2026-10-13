"""Mini Recipe Book: 10 features."""
import json

recipes = {}
def add_recipe(name, ingredients, instructions, category="General"):  # 1
    recipes[name] = {"ingredients": list(ingredients), "instructions": instructions, "category": category}
def get_recipe(name):  # 2
    return recipes.get(name)
def search_recipes(keyword):  # 3
    k = keyword.casefold()
    return {n:r for n,r in recipes.items() if k in n.casefold() or k in r["instructions"].casefold()}
def filter_by_category(category):  # 4
    return {n:r for n,r in recipes.items() if r["category"].casefold() == category.casefold()}
def recipes_using(ingredient):  # 5
    i = ingredient.casefold()
    return [n for n,r in recipes.items() if any(i == x.casefold() for x in r["ingredients"])]
def ingredient_list(name):  # 6
    r = get_recipe(name)
    return list(r["ingredients"]) if r else []
def shopping_list(names):  # 7
    items = set()
    for n in names:
        r = get_recipe(n)
        if r:
            items.update(x.strip() for x in r["ingredients"] if x.strip())
    return sorted(items, key=str.casefold)
def remove_recipe(name):  # 8
    return recipes.pop(name, None) is not None
def recipe_count():  # 9
    return len(recipes)
def export_json(filename="recipes.json"):  # 10
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(recipes, f, indent=2, ensure_ascii=False)
    return filename

if __name__ == "__main__":
    add_recipe("Vegetable Sandwich", ["bread", "tomato", "cucumber"], "Layer vegetables between bread.", "Snack")
    add_recipe("Tomato Salad", ["tomato", "onion", "salt"], "Chop and mix.", "Salad")
    print("Tomato recipes:", recipes_using("tomato"))
    print("Shopping list:", shopping_list(list(recipes)))
