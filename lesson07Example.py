def basket_total(*prices):
    return sum(prices)

def items_total(**items):
    return len(items)


names = ["popcorn","porkbelly","beef","peach","apple"]
items = [("popcorn",10000),("porkbelly",20000),("beef",50000),
        ("peach",12000),("apple",14000)]


print(basket_total(10000,20000,50000,12000,15000))
print(sorted(names, key=lambda names: len(names)))
print(sorted(items, key=lambda items: len(items)))

