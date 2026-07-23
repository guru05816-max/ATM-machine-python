# ATM-machine-python

# ATM Machine — Python Console Application

A rule-based ATM application built in Python using `if-elif-else` decision logic to handle balance enquiry, deposit, and withdrawal — the same structured, condition-driven thinking used in AI decision logic and simple rule-based systems.

## Features

- 🔐 **PIN Authentication** — 3 attempts before access is blocked
- 💰 **Balance Enquiry** — check current account balance
- 💵 **Deposit** — add money with validation (positive amount, upper limit check)
- 🏧 **Withdraw** — cash withdrawal with checks for minimum balance, per-transaction limit, and multiples of ₹100
- 🔑 **Change PIN** — securely update the account PIN
- ♻️ **Menu-driven loop** — keeps running until the user chooses to exit

## Tech Stack

`Python` `PyCharm` `VS Code`

## How It Works

The application uses simple `if-elif-else` conditional logic (no external libraries or database) to simulate real-world ATM decision-making:

- Every transaction is validated against a set of rules before it's approved
- Invalid inputs, insufficient balance, and limit violations are handled gracefully
- Menu-driven interface keeps the flow interactive and easy to follow

## How to Run

```bash
python3 atm_machine.py
```

**Default credentials:**
- PIN: `1234`
- Starting Balance: ₹5,000

## Sample Menu

```
1. Balance Enquiry
2. Deposit
3. Withdraw
4. Change PIN
5. Exit
```

## What I Learned

Building this project helped me practice structured, condition-driven logic — breaking down a real-world process (ATM operations) into clear rules and decision branches, similar to how rule-based systems and basic AI decision logic work.

## Author

**Guruprasanth K**
