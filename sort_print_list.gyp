# Building three functions: sort, reverse sort, and print list

pizza_toppings = [
    'Hawaiian',
    'Champagne Ham & CheeseBeef & Onion',
    'Pepperoni',
    'Simply Cheese',
    'Bacon & Mushroom',
    'Italiano',
    'The Deluxe',
    'Ham, Egg & Hollandaise',
    'Americano',
    'Mr Wedge',
    'BBQ Meatlovers'
]

def sort_list(lst): #defining function sort_list that takes 1 parameter called lst
   return sorted(lst, key=str.lower) #sorting lst case insensitive without changing the list

def sort_reverse_list(lst): #defining function sort_reverse_list that takes 1 parameter called lst
    return [ele for ele in reversed(sorted(lst, key=str.lower))] #reverse sorting lst case insensitive without changing the list

def print_list(lst): #defining function print_list that takes 1 parameter called lst
    for i in sorted(lst, key=str.lower): #iterating, sorting lst case insensitive
        print (i) #printing each element in sorted list

print(pizza_toppings)
print("\n")
print(sort_list(pizza_toppings))
print("\n")
print(sort_reverse_list(pizza_toppings))
print("\n")
print_list(pizza_toppings)