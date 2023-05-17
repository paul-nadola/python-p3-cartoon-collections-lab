cartoons = ["Doc", "Dopey", "Bashful", "Grumpy"]
def roll_call_dwarves(cartoons):
    for i, cartoon in enumerate(cartoons, start= 1):
        print(f"{i}. {cartoon}")

print (roll_call_dwarves(cartoons))

planeteer_calls = ["earth", "wind", "fire", "water", "heart"]

def summon_captain_planet(planeteer_calls):
    cap_planeteer_calls = []
    for call in planeteer_calls:
        new_call = call.capitalize() + "!"
        cap_planeteer_calls.append(new_call)
    return cap_planeteer_calls

print(summon_captain_planet(planeteer_calls))


def long_planeteer_calls(calls):
    # if len(calls) < 4:
    #     return False
    if len(calls) == 4:
        return True
    else:
        return False
    

def find_the_cheese(ingredients):
    cheeses = ["cheddar", "gouda", "camembert"]
    
    for ingredient in ingredients:
        if ingredient in cheeses:
            return ingredient
    
    return None
