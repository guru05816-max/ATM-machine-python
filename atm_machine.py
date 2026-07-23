"""
ATM Machine — Python Console Application
------------------------------------------
A simple rule-based ATM simulator using if-elif-else decision logic
to handle balance enquiry, deposit, and withdrawal operations.

This mirrors the same structured, condition-driven thinking used in
AI decision logic and simple rule-based systems.
"""

# ------------------------------
# Initial account setup
# ------------------------------
account_pin = "1234"
balance = 5000.0
MIN_BALANCE = 0
MAX_WITHDRAW_PER_TXN = 25000


def print_header():
    print("=" * 40)
    print("       WELCOME TO PYTHON ATM")
    print("=" * 40)


def authenticate():
    """Give the user 3 attempts to enter the correct PIN."""
    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN: ").strip()

        if entered_pin == account_pin:
            print("\n✅ PIN accepted. Access granted.\n")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"❌ Incorrect PIN. Attempts left: {attempts}\n")
            else:
                print("❌ Too many incorrect attempts. Card blocked.\n")

    return False


def show_menu():
    print("-" * 40)
    print("1. Balance Enquiry")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")
    print("5. Exit")
    print("-" * 40)


def balance_enquiry(bal):
    print(f"\n💰 Your current balance is: ₹{bal:.2f}\n")


def deposit(bal):
    try:
        amount = float(input("Enter amount to deposit: ₹"))
    except ValueError:
        print("\n❌ Invalid input. Please enter a numeric amount.\n")
        return bal

    if amount <= 0:
        print("\n❌ Deposit amount must be greater than zero.\n")
    elif amount > 200000:
        print("\n❌ Single deposit limit exceeded (max ₹2,00,000).\n")
    else:
        bal += amount
        print(f"\n✅ ₹{amount:.2f} deposited successfully.")
        print(f"💰 New balance: ₹{bal:.2f}\n")

    return bal


def withdraw(bal):
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
    except ValueError:
        print("\n❌ Invalid input. Please enter a numeric amount.\n")
        return bal

    if amount <= 0:
        print("\n❌ Withdrawal amount must be greater than zero.\n")
    elif amount % 100 != 0:
        print("\n❌ Please enter an amount in multiples of ₹100.\n")
    elif amount > MAX_WITHDRAW_PER_TXN:
        print(f"\n❌ Withdrawal limit exceeded. Max ₹{MAX_WITHDRAW_PER_TXN} per transaction.\n")
    elif amount > bal:
        print(f"\n❌ Insufficient balance. Available balance: ₹{bal:.2f}\n")
    elif (bal - amount) < MIN_BALANCE:
        print(f"\n❌ Transaction denied. Minimum balance of ₹{MIN_BALANCE} must be maintained.\n")
    else:
        bal -= amount
        print(f"\n✅ ₹{amount:.2f} withdrawn successfully. Please collect your cash.")
        print(f"💰 New balance: ₹{bal:.2f}\n")

    return bal


def change_pin():
    global account_pin
    old_pin = input("Enter current PIN: ").strip()

    if old_pin != account_pin:
        print("\n❌ Current PIN is incorrect. PIN not changed.\n")
        return

    new_pin = input("Enter new 4-digit PIN: ").strip()
    confirm_pin = input("Confirm new PIN: ").strip()

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("\n❌ PIN must be exactly 4 digits.\n")
    elif new_pin != confirm_pin:
        print("\n❌ PINs do not match. PIN not changed.\n")
    else:
        account_pin = new_pin
        print("\n✅ PIN changed successfully.\n")


def main():
    global balance

    print_header()

    if not authenticate():
        print("Exiting... Thank you.")
        return

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            balance_enquiry(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            change_pin()
        elif choice == "5":
            print("\n🙏 Thank you for using Python ATM. Visit again!")
            break
        else:
            print("\n❌ Invalid option. Please choose between 1 and 5.\n")


if __name__ == "__main__":
    main()
