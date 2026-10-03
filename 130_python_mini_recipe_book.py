# 130_python_mini_recipe_book.py
# Mini Recipe Book - 10 practical features
recipes = {
    "Pancakes":{"ingredients":["flour","milk","egg"],"minutes":20,"vegetarian":True},
    "Pasta":{"ingredients":["pasta","tomato","cheese"],"minutes":30,"vegetarian":True},
    "Omelette":{"ingredients":["egg","salt","pepper"],"minutes":10,"vegetarian":False},
    "Fruit Salad":{"ingredients":["apple","banana","orange"],"minutes":10,"vegetarian":True},
}
print("1. Recipes:",recipes)
print("2. Recipe count:",len(recipes))
keyword="pasta"; print("3. Search:",[n for n in recipes if keyword in n.lower()])
print("4. Quick recipes:",[n for n,r in recipes.items() if r["minutes"]<=15])
print("5. Vegetarian:",[n for n,r in recipes.items() if r["vegetarian"]])
print("6. Pasta ingredients:",recipes["Pasta"]["ingredients"])
print("7. By cooking time:",sorted(recipes.items(),key=lambda x:x[1]["minutes"]))
ingredient="egg"; print("8. Recipes with egg:",[n for n,r in recipes.items() if ingredient in r["ingredients"]])
recipes["Vegetable Soup"]={"ingredients":["carrot","peas","water"],"minutes":25,"vegetarian":True}
print("9. Added recipe:",recipes["Vegetable Soup"])
minutes=sum(r["minutes"] for r in recipes.values())
print("10. Summary:",{"recipes":len(recipes),"average_cooking_minutes":round(minutes/len(recipes),2)})
