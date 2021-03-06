# Creating dictionary and printing the contents

macaron_ingredients_lookup = { # creating dictionary
    "almond flour - cup": 1, # "key": value,
    "confectioners sugar - cup": 1.75,
    "salt - tsp": 1,
    "egg whites": 3,
    "sugar - cup": 0.25,
    "vanilla extract - tsp": 0.5,
    "food coloring - drop": 2
}

filling_ingredients_lookup = {
    "unsalted butter - cup": 1,
    "confectioners sugar - cup": 3,
    "vanilla extact - tsp": 1,
    "heavy cream - tbsp": 3
}

print ("Macaron ingredients:") 
for key, value in macaron_ingredients_lookup.items(): # iterating key and value
    print(key, ':', value)

print ("\nButtercream filling ingredients:") 
for key, value in filling_ingredients_lookup.items():
    print(key, ':', value)