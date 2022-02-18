class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceinquiry(self):
        print("Your Balance is: $1000000")

    def cashwithdraw(self, amount):
        new_amount = 1000000-amount
        print("You withdrawled: "+ str(amount) + "Your remaining balnce is: " + str(new_amount))

def main():
    name = input("Hello what is your name?: ")
    print("Hello, " + name)
    cardnumber = input("Insert your card number: ")
    pin = input("Enter your pin: ")
    new_user = Atm(cardnumber, pin)

    print("Choose your activity: ")
    print("1. Balance Inquiry")
    print("2. Cash Withdrawal")
    activity = int(input("Enter Activity Choice: "))

    if (activity == 1):
        new_user.balanceinquiry()
    elif (activity == 2):
        amount = int(input("Enter the amount: "))
        new_user.cashwithdraw(amount)
    else:
        print("Enter a valid number: ")

if __name__ == "__main__":
    main()
    
