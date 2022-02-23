print("Welcome to my shop")
print("What do you want to buy?")
cart = []
item_init = {
    "name": "",
    "unitPrice": 0,
    "quantity": 0,
    "total_price": 0
}

def shopping():
    name = input("Enter the name of the item: ")
    pu = float(input("How much does the item cost? "))
    qty = int(input("How many items did you buy? "))
    total_price = pu * qty
    item = item_init.copy()
    item["name"] = name
    item["unitPrice"] = pu
    item["quantity"] = qty
    item["total_price"] = total_price
    return item

item = shopping()
cart.append(item)

response = input("Do you want to proceed your shopping?\n\t Yes/No? ")

while response.lower() == "yes":
    item = shopping()
    cart.append(item)
    response = input("Do you want to proceed your shopping?\n\t Yes/No? ")

f = open("bill.txt", "w")
f.write("Your bill is ready!!\n")
bill = 0
for product in cart:
    bill += product["total_price"]
    for key, value in product.items():
        f = open("bill.txt", "a")
        f.write("\n\t\t{} : \t{}".format(key, value))
    f.write("\n\t\t\t ******************")

f.write("\n\nYou have to pay:\t\t\t\t {}FCFA".format(bill))
f.close()

print(f'You have to pay: \t{bill}FCFA')
print("Thanks for your purchase. See you soon!")


