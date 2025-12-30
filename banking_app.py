# Banking Program
# Features: deposit, withdraw, balance check, and input validation

balance = 0
print("welcome to CBE bank!".upper())


def show_balance():
    print(f"your Balance is : $ {balance}")


def deposit(amount):
    global balance
    balance += amount
    print(f"deposited amount: ${amount:2f} .your current Balance is: $ {balance}")


def withdraw(amount):
    global balance

    if 0 < amount < balance:
        balance -= amount
        print(f"withdrew amount: ${amount:2} .your Balance is: $ {balance}")
    elif amount > balance:
        print("You don't have enough money.")
    elif amount < 0:
        print("the amount must be positive.".title())
    else:
        print("invalid amount")


running = True
while running:
    print(" 1.to balance\n", "2.to deposit\n", "3.to withdraw\n", '4.to Exite'.title())
    try:
        choice =float(input('enter your choice (1-4):'))

        if choice == 1:
            show_balance()
        elif choice ==    2:
            amt = float(input("enter your amount: $"))
            deposit(amt)
        elif choice == 3:
            amt = float(input("enter your amount: $"))
            withdraw(amt)
        elif choice == 4:
            running = False
        else:
            print("the input value is out of range. \n please try again.")
    except ValueError:
        print("invalid input.\nplease try again.")

print("thank you for your trust have nice day")
