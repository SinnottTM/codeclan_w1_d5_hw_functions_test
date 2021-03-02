# WRITE YOUR FUNCTIONS HERE

# Function to get pet's name
def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]

# Functions to get total cash
def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]

# Function to add or remove cash via accessing admin
def add_or_remove_cash(cc_pet_shop, cash):
    cash_total = cc_pet_shop["admin"]["total_cash"]
    cash_total += cash
    cc_pet_shop["admin"]["total_cash"] = cash_total

# Function to see total number of pets already sold
def get_pets_sold(cc_pet_shop):
    return cc_pet_shop["admin"]["pets_sold"]

# Function to tell program to update number of pets sold 
def increase_pets_sold(cc_pet_shop, pets_sold_num):
    cc_pet_shop["admin"]["pets_sold"] += pets_sold_num

# Function to get the stock count (use length on pets itself, as this will contain the total number of pets)
def get_stock_count(cc_pet_shop):
    return len(cc_pet_shop["pets"])

# Function to check all dogs of a particular breed
def get_pets_by_breed(cc_pet_shop, breed):
    pets_of_breed_list = []
    for pet in cc_pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_of_breed_list.append(pet)
    return pets_of_breed_list

# Function to get the name of a pet
def find_pet_by_name(cc_pet_shop, pet_name):
    for pet in cc_pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
        # else:
        #     return None

# Function to remove pet by name (mutliple options)
def remove_pet_by_name(cc_pet_shop, pet_name):
    # if you want to use index, it is more complex and operates on index numbers, so you must tell the loop to cycle by index
    # index = 0
    # for pet in cc_pet_shop["pets"]:
    #     if pet["name"] == pet_name:
    #         cc_pet_shop["pets"].pop(index)
    #     else:
    #         index += 1
    for pet in cc_pet_shop["pets"]:
        if pet["name"] == pet_name:
            del(cc_pet_shop[pet])
            # following also works
            # cc_pet_shop["pet"].remove(pet)
            
# Function to add new pet to the pet shop
def add_pet_to_stock(cc_pet_shop, new_pet):
    cc_pet_shop["pets"].append(new_pet)

# Function to get customer cash
def get_customer_cash(customers):
    return customers["cash"]

# Function to charge customers 
def remove_customer_cash(customers, amount):
    customers["cash"] -= amount

# Function to get the number of pets
def get_customer_pet_count(customers):
    return len(customers["pets"])

# Function to give a pet to a customer
def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)

# Function to see if customer can afford a pet
def customer_can_afford_pet(customers, new_pet):
    return new_pet["price"] <= customers["cash"]

# Function to sell pet to customer
# Use previous functions in combination (modular?)
# Includes an ability to check for 
def sell_pet_to_customer(cc_pet_shop, pet_name, customer_name):
    # initial attempt, didn't work
    # if pet_name != find_pet_by_name(cc_pet_shop, pet_name):
    #   return None
    if pet_name == None:
        return None
    # 
    if customer_can_afford_pet(customer_name, pet_name):
        pet_cost = pet_name["price"]
        add_pet_to_customer(customer_name, pet_name)
        remove_pet_by_name(cc_pet_shop, pet_name)
        remove_customer_cash(customer_name, pet_cost)
        increase_pets_sold(cc_pet_shop, 1)
        add_or_remove_cash(cc_pet_shop, pet_cost)

# Notes on improving
# Pet_name should be pet, it is a bet object and not just the name
# cc_pet_shop should be called per_shop so it can be re-useable
# add_or_remove_cash could use the same logic as increase_pets_sold, neater and cleaner
# Generally pretty good, just need to remember that at this point, trying to proof apps so they don't break isn't really needed (not at that layer yet)
    
