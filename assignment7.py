items={"milk":25,"egg":6,"bread":20,"yogurt":45,"oats":78}
product=input("Enter the product name")
for price in items:
    if product==price:
        print(items.get(price))


