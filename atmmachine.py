class ATM:
    def __init__(self):
        self.balance = 5000
        self.pin = 1234

    def check_pin(self, input_pin):
        if input_pin == self.pin:
            print("🔓 PIN accepted. WELCOME!🎉")
            return True
        else:
            print("🔒 PIN incorrect. Please try again.❌")
            return False

    def check_balance(self):
        print(f"💰 Your current balance is: Rs. {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("❌ Deposit amount must be greater than 0.")
        else:
            self.balance += amount
            print(f"✅ Rs. {amount} deposited successfully!!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient balance.")
        elif amount <= 0:
            print("❌ Withdraw amount must be greater than 0.")
        else:
            self.balance -= amount
            print(f"✅ Rs. {amount} withdraw successfully!!")

    def exit(self):
        print("👋 Thank you for using the ATM. Goodbye!")

#Program Start
atm = ATM()

print("🔐 Welcome to the ATM!")
user_pin = int(input("Please enter your 4-digit PIN: "))

if atm.check_pin(user_pin):
    while True:
        print("\nChoose an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            atm.check_balance()

        elif choice == "2":
            amount = int(input("Enter amount to deposit: Rs. "))
            atm.deposit(amount)

        elif choice == "3":
            amount = int(input("Enter amount to withdraw: Rs. "))
            atm.withdraw(amount)

        elif choice == "4":
            atm.exit()

        else:
            print("❌ Invalid choice. Please try again.")
