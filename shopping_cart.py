
# create shopping that asks user for item and price of item
# have exit clause, if customer is done adding items to cart
# at the end show items and total cost

foods = []
prices = []
total = 0

while True:
    food = input("Enter food to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter price of {food}: R"))
        foods.append(food)
        prices.append(price)
        
print("----YOUR CART----")

for food in foods:
    print(food, end= " ")
    
total = sum(prices)

print("\n")   
print(f"Your total is: R{total}")
    