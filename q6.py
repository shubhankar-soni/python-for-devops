# You are building a simple transaction processor. You start with a balance = 500.
# Given a list of transactions where positive numbers are deposits and negative numbers are withdrawals:
# transactions = [200, -50, -800, 150, -40, -1000]

# Iterate through the list and update the balance according to these rules:

# If it's a deposit (positive number), add it to the balance and print: "Deposited $[amount]. New balance: $[balance]"

# If it's a withdrawal (negative number), check if there are enough funds.

# If balance is greater than or equal to the withdrawal amount, subtract it and print: "Withdrew $[amount]. New balance: $[balance]"

# If the withdrawal exceeds the balance, do not subtract it, and print: "Transaction declined: Insufficient funds for $[amount] withdrawal."
## Implement from below line: ##

balance = 500
transactions = [200, -50, -800, 150, -40, -1000]

for i in transactions:
    if i < 0 :
        if balance >= abs(i) :
            balance = balance + i
            print(f"Withdrew ${i} New balance: ${balance}")
        else:
            print(f"Transaction declined: Insufficient funds for ${abs(i)} withdrawal. Current balance is {balance}")    
    elif i > 0 :
        balance = balance + i
        print(f"Deposited ${i}. New Balance is ${balance}")
    