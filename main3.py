def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if "sydney" == city:
        return 183
    elif "dubai" == city:
        return 220
    elif "england" == city:
        return 475
def rental_car_cost(days):
    if days>=7:
        return 40*days -50
    elif days>=3:
        return 40*days - 20
    else:
     return 40*days
def trip_cost(city,days,spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)+ spending_money
print("cost of car rental:", rental_car_cost)
print("cost of plane ride:", plane_ride_cost("sydney"))  
print("cost of hotel room:", hotel_cost(14)) 
print("total cost of the trip:", trip_cost("sydney" ,7,1500))
print(trip_cost("dubai", 6,500))
    
    
    