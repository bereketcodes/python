# MENU

menu = {"hot dogs" : 45,
        "popcorn" : 34,
        "drink" : 12,
        "pizza" : 22,
        "burger" : 56
        }
cart = []

total = 0
print (  " "+"="*4 + "🍠🧀🍊" * 3 + "=" * 3 +
       "\n welcome to ower hotel! please order you choice from menu below 🧀🍊💜" .upper())

__running = True
for keys, values in menu.items():
    print(f"  {keys:9} : {values:.2f}")

print(" " "="*11)
while __running:
    choice = input("Enter your choice (q to quit): ").lower().strip()
    if choice == 'q':
        print("thank you for shopping".title())
        break
    elif menu.get(choice) is not None:
        cart.append(choice)
    elif menu.get(choice) is None:
        print("Sorry, we don't have this options : please choice from menu")
        continue


    total += menu.get(choice)
print("-"*10 + "your cart".upper()+"-"*10)
for food in cart:
    print(f" {food:5}: ${menu.get(food)}")
    # total = total + food
print(f"total cost: ${total:.2f}".title())

print("-"*15)




