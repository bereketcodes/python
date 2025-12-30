def pad ():
    pad_num=((1, 2, 3)
         ,(4, 5, 6)
         ,(7, 8, 9)
         ,("*",0, "#"))
    for row in pad_num:
        for col in row:
            print(col, end=" ")
        print()

def shop_cart():

    foods = []
    prices = []
    total_price = 0
    while True:
         choice=input("Enter your food choice('q' to quit):")
         if choice.lower()=="q":
             break

         else:
             price = int(input("Enter your price:$ "))
             foods.append(choice)
             prices.append(price)
         # total_price += prices

    print("----your cart----".upper())

    for food in foods:
        print(food, end=", ".rstrip())
    print()
    for price in prices:
        total_price += price
    print(f"total price :${total_price}".title())

"""calling both function  Alternatively"""

# pad()
# shop_cart()
