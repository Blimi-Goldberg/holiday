# defining functions to calculate a cost of a holiday
def hotel_cost(x):   # hotel cost takes the argument of amount of days and multiplys by 100
    y = x * 100
    return y 
def plane_cost(y):  # depending where we are travelling to the function calculates a cost
    if y == "las vegas":
        return 325
    elif y == "london":
        return 250
    else:
        return 189
def car_rental(z):  # takes an argument of amount of days and multiplys by 50
    y = z * 50
    return y
def holiday_cost(x, y, z):  # calculates total cost of holiday
    total = hotel_cost(x) + plane_cost(y) + car_rental(z)
    return total

x = int(input("how many days are you staying in the hotel? "))
y = input("where are you travelling to? (las vegas, london or other) ").lower()
z = int(input("how many days are you renting a car for? "))
print(f"""The total cost of your holiday is £{holiday_cost(x,y,z)}, your hotel stay is costing £{hotel_cost(x)},
your plane is costing £{plane_cost(y)} and your car is costing £{car_rental(z)}. Enjoy!""")