import copy

print("Welcome to my shop")
print("What do you want to buy?")
cart = []
item = {
    "name": "",
    "unitPrice": 0,
    "quantity": 0,
    "total_price": 0
}


def shopping():
    name = input("Enter the name of the item: ")
    pu = int(input("How much does the item cost? "))
    qty = int(input("How many items did you buy? "))
    total_price = pu * qty

    article = item.copy()
    article["name"] = name
    article["unitPrice"] = pu
    article["quantity"] = qty
    article["total_price"] = total_price

    return article


new = shopping()
cart.append(new)

response = input("Do you want to proceed your shopping?\n\t Yes/No? ")

while response.lower() == "yes":
    buy = shopping()
    cart.append(buy)
    response = input("Do you want to proceed your shopping?\n\t Yes/No? ")
    

bill = 0
for items in cart:
    print(items)
    bill += items["total_price"]

print(f'You have to pay: \t{bill}FCFA')
print("Thanks for your purchase. See you soon!")


