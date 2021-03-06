# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, increase):
    # can i call get_pets_sold(pet_shop) and increase that?
    # no, get_pets_sold(pet_shop) returns an int, not a reference to the dictionary itself. increasing that returned value will not cause the dictionary to update
    pet_shop["admin"]["pets_sold"] += increase


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets.append(pet)
    return pets


def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet


def remove_pet_by_name(pet_shop, name):
    pet_to_remove = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].remove(pet_to_remove)


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, amount):
    customer["cash"] -= amount


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)


# optional test functions
def customer_can_afford_pet(customer, new_pet):
    return customer["cash"] >= new_pet["price"]


# integration tests
def sell_pet_to_customer(pet_shop, pet, customer):
    if pet is not None:
        got_funds = customer_can_afford_pet(customer, pet)
        if got_funds:
            add_pet_to_customer(customer, pet)
            increase_pets_sold(pet_shop, 1)
            price = pet["price"]
            remove_customer_cash(customer, price)
            add_or_remove_cash(pet_shop, price)
            # not tested, but can't sell the pet twice!
            remove_pet_by_name(pet_shop, pet["name"])
