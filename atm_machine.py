"""
╔══════════════════════════════════════════╗
║        ATM MACHINE — Python CLI          ║
║   Features: Login, Deposit, Withdraw,    ║
║   Balance, Transfer, PIN Change,         ║
║   Transaction History, Multiple Accounts ║
╚══════════════════════════════════════════╝
"""

import datetime
import os

# ── DATABASE (Multiple Accounts) ──────────────────────────────────────────────
accounts = {
    "1001": {
        "name": "Guru Max",
        "pin": "1234",
        "balance": 50000.00,
        "transactions": [
            {"type": "Initial Deposit", "amount": 50000.00, "date": "2026-01-01 09:00:00"},
        ],
    },
    "1002": {
        "name": "Test User",
        "pin": "5678",
        "balance": 25000.00,
        "transactions": [
            {"type": "Initial Deposit", "amount": 25000.00, "date": "2026-01-01 09:00:00"},
        ],
    },
}

MAX_PIN_ATTEMPTS = 3

# ── HELPERS ───────────────────────────────────────────────────────────────────
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def fmt(amount):
    return f"₱{amount:,.2f}"

def line(char="─", length=44):
    print(char * length)

def header(title="ATM MACHINE"):
    clear()
    line("═")
    print(f"{'🏧  ' + title:^44}")
    line("═")

def press_enter():
    input("\n  Press Enter to continue...")

def add_transaction(acc_no, t_type, amount):
    accounts[acc_no]["transactions"].append({
        "type": t_type,
        "amount": amount,
        "date": now(),
    })

# ── LOGIN ─────────────────────────────────────────────────────────────────────
def login():
    attempts = 0
    while True:
        header("WELCOME")
        print("\n  Insert your Account Number")
        print("  (or type 'exit' to quit)\n")
        acc_no = input("  Account No: ").strip()

        if acc_no.lower() == "exit":
            print("\n  Thank you for using our ATM. Goodbye!\n")
            exit()

        if acc_no not in accounts:
            print("\n  ❌ Account not found!")
            press_enter()
            continue

        # PIN verification
        pin_attempts = 0
        while pin_attempts < MAX_PIN_ATTEMPTS:
            header("PIN ENTRY")
            print(f"\n  Account: {acc_no}")
            remaining = MAX_PIN_ATTEMPTS - pin_attempts
            print(f"  Attempts remaining: {remaining}\n")
            pin = input("  Enter PIN: ").strip()

            if pin == accounts[acc_no]["pin"]:
                print(f"\n  ✅ Welcome, {accounts[acc_no]['name']}!")
                press_enter()
                return acc_no
            else:
                pin_attempts += 1
                if pin_attempts < MAX_PIN_ATTEMPTS:
                    print("\n  ❌ Incorrect PIN. Try again.")
                    press_enter()
                else:
                    print("\n  🔒 Card blocked! Too many incorrect attempts.")
                    press_enter()
                    break

# ── BALANCE ENQUIRY ───────────────────────────────────────────────────────────
def check_balance(acc_no):
    header("BALANCE ENQUIRY")
    acc = accounts[acc_no]
    print(f"\n  Account Holder : {acc['name']}")
    print(f"  Account Number : {acc_no}")
    line()
    print(f"  Available Balance : {fmt(acc['balance'])}")
    line()
    press_enter()

# ── DEPOSIT ───────────────────────────────────────────────────────────────────
def deposit(acc_no):
    header("CASH DEPOSIT")
    acc = accounts[acc_no]
    print(f"\n  Current Balance: {fmt(acc['balance'])}\n")

    try:
        amount = float(input("  Enter deposit amount: ₱"))
        if amount <= 0:
            print("\n  ❌ Amount must be greater than zero.")
            press_enter()
            return
        if amount > 1000000:
            print("\n  ❌ Maximum deposit limit is ₱1,000,000.")
            press_enter()
            return

        acc["balance"] += amount
        add_transaction(acc_no, "Deposit", amount)

        print(f"\n  ✅ Successfully deposited {fmt(amount)}")
        print(f"  New Balance: {fmt(acc['balance'])}")
        line()
    except ValueError:
        print("\n  ❌ Invalid amount entered.")
    press_enter()

# ── WITHDRAW ──────────────────────────────────────────────────────────────────
def withdraw(acc_no):
    header("CASH WITHDRAWAL")
    acc = accounts[acc_no]
    print(f"\n  Available Balance: {fmt(acc['balance'])}\n")

    # Quick amount menu
    print("  Quick Select:")
    quick = [500, 1000, 2000, 5000, 10000]
    for i, q in enumerate(quick, 1):
        print(f"  [{i}] {fmt(q)}")
    print("  [6] Other Amount")
    print("  [0] Cancel\n")

    choice = input("  Choose: ").strip()

    if choice == "0":
        return
    elif choice in [str(i) for i in range(1, 6)]:
        amount = quick[int(choice) - 1]
    elif choice == "6":
        try:
            amount = float(input("  Enter amount: ₱"))
        except ValueError:
            print("\n  ❌ Invalid amount.")
            press_enter()
            return
    else:
        print("\n  ❌ Invalid choice.")
        press_enter()
        return

    if amount <= 0:
        print("\n  ❌ Amount must be greater than zero.")
        press_enter()
        return
    if amount > acc["balance"]:
        print(f"\n  ❌ Insufficient balance!")
        print(f"  Available: {fmt(acc['balance'])}")
        press_enter()
        return
    if amount > 50000:
        print("\n  ❌ Maximum withdrawal limit per transaction is ₱50,000.")
        press_enter()
        return

    acc["balance"] -= amount
    add_transaction(acc_no, "Withdrawal", amount)

    print(f"\n  ✅ Please collect your cash.")
    print(f"  Amount Withdrawn : {fmt(amount)}")
    print(f"  Remaining Balance: {fmt(acc['balance'])}")
    line()
    press_enter()

# ── FUND TRANSFER ─────────────────────────────────────────────────────────────
def transfer(acc_no):
    header("FUND TRANSFER")
    acc = accounts[acc_no]
    print(f"\n  Your Balance: {fmt(acc['balance'])}\n")

    to_acc = input("  Enter recipient account number: ").strip()

    if to_acc == acc_no:
        print("\n  ❌ Cannot transfer to your own account.")
        press_enter()
        return
    if to_acc not in accounts:
        print("\n  ❌ Recipient account not found.")
        press_enter()
        return

    print(f"  Recipient: {accounts[to_acc]['name']}")

    try:
        amount = float(input("  Enter transfer amount: ₱"))
    except ValueError:
        print("\n  ❌ Invalid amount.")
        press_enter()
        return

    if amount <= 0:
        print("\n  ❌ Amount must be greater than zero.")
        press_enter()
        return
    if amount > acc["balance"]:
        print(f"\n  ❌ Insufficient balance!")
        press_enter()
        return

    # Confirm
    print(f"\n  ── Transfer Summary ──")
    print(f"  To      : {accounts[to_acc]['name']} ({to_acc})")
    print(f"  Amount  : {fmt(amount)}")
    confirm = input("\n  Confirm transfer? (yes/no): ").strip().lower()

    if confirm != "yes":
        print("\n  ❌ Transfer cancelled.")
        press_enter()
        return

    acc["balance"] -= amount
    accounts[to_acc]["balance"] += amount
    add_transaction(acc_no, f"Transfer to {to_acc}", amount)
    add_transaction(to_acc, f"Transfer from {acc_no}", amount)

    print(f"\n  ✅ Transfer successful!")
    print(f"  New Balance: {fmt(acc['balance'])}")
    line()
    press_enter()

# ── TRANSACTION HISTORY ───────────────────────────────────────────────────────
def transaction_history(acc_no):
    header("TRANSACTION HISTORY")
    acc = accounts[acc_no]
    txns = acc["transactions"]

    if not txns:
        print("\n  No transactions found.")
        press_enter()
        return

    print(f"\n  Account: {acc['name']} ({acc_no})")
    line()
    print(f"  {'TYPE':<25} {'AMOUNT':>12}  DATE")
    line()

    # Show last 10 transactions
    for txn in reversed(txns[-10:]):
        t = txn["type"][:24]
        a = fmt(txn["amount"])
        d = txn["date"]
        print(f"  {t:<25} {a:>12}  {d}")

    line()
    print(f"  Total transactions: {len(txns)}")
    print(f"  Current Balance   : {fmt(acc['balance'])}")
    line()
    press_enter()

# ── CHANGE PIN ────────────────────────────────────────────────────────────────
def change_pin(acc_no):
    header("CHANGE PIN")

    current = input("\n  Enter current PIN: ").strip()
    if current != accounts[acc_no]["pin"]:
        print("\n  ❌ Incorrect current PIN!")
        press_enter()
        return

    new_pin = input("  Enter new PIN (4 digits): ").strip()
    if not new_pin.isdigit() or len(new_pin) != 4:
        print("\n  ❌ PIN must be exactly 4 digits!")
        press_enter()
        return

    confirm_pin = input("  Confirm new PIN: ").strip()
    if new_pin != confirm_pin:
        print("\n  ❌ PINs do not match!")
        press_enter()
        return

    accounts[acc_no]["pin"] = new_pin
    print("\n  ✅ PIN changed successfully!")
    print("  Please remember your new PIN.")
    press_enter()

# ── MINI STATEMENT ────────────────────────────────────────────────────────────
def mini_statement(acc_no):
    header("MINI STATEMENT")
    acc = accounts[acc_no]
    txns = acc["transactions"][-5:]  # Last 5 only

    print(f"\n  {acc['name']} | {acc_no}")
    line()
    for txn in reversed(txns):
        print(f"  {txn['date']}")
        print(f"  {txn['type']:<30} {fmt(txn['amount']):>10}")
        line("·")
    print(f"\n  Balance: {fmt(acc['balance'])}")
    line()
    press_enter()

# ── MAIN MENU ─────────────────────────────────────────────────────────────────
def main_menu(acc_no):
    acc = accounts[acc_no]
    while True:
        header("MAIN MENU")
        print(f"\n  Welcome, {acc['name']}")
        print(f"  Balance: {fmt(acc['balance'])}")
        line()
        print("  [1] 💰 Check Balance")
        print("  [2] 📥 Deposit Cash")
        print("  [3] 📤 Withdraw Cash")
        print("  [4] 🔄 Fund Transfer")
        print("  [5] 📋 Transaction History")
        print("  [6] 🧾 Mini Statement")
        print("  [7] 🔑 Change PIN")
        print("  [8] 🚪 Logout")
        line()
        choice = input("  Select option: ").strip()

        if choice == "1":
            check_balance(acc_no)
        elif choice == "2":
            deposit(acc_no)
        elif choice == "3":
            withdraw(acc_no)
        elif choice == "4":
            transfer(acc_no)
        elif choice == "5":
            transaction_history(acc_no)
        elif choice == "6":
            mini_statement(acc_no)
        elif choice == "7":
            change_pin(acc_no)
        elif choice == "8":
            header("LOGOUT")
            print(f"\n  Thank you, {acc['name']}!")
            print("  Please take your card.")
            print("  Have a great day! 👋\n")
            line()
            press_enter()
            break
        else:
            print("\n  ❌ Invalid option. Please try again.")
            press_enter()

# ── ENTRY POINT ───────────────────────────────────────────────────────────────
def main():
    while True:
        acc_no = login()
        main_menu(acc_no)
        # After logout, ask to continue or exit
        header("ATM MACHINE")
        print("\n  [1] New Transaction")
        print("  [2] Exit\n")
        again = input("  Choose: ").strip()
        if again != "1":
            clear()
            print("\n  Thank you for using our ATM!")
            print("  Goodbye! 👋\n")
            break

if __name__ == "__main__":
    main()
