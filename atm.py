print("======== ATM ==========")
print("1.Check Balance")
print("2.Deposite Money")
print("3.Withdraw Money")

choice = int(input("Enter your choice:"))

balance = 30000

if choice == 1:
    print("Balance:" , balance)

elif choice == 2:
    deposit_amount = int(input("Enter the deposit amount:"))
    updated_balance = deposit_amount + balance
    print("Updated balance:", updated_balance)

elif choice == 3:
    withdraw_amount = int(input("Enter the withdraw amount:"))

    if withdraw_amount > balance:
        print("Insufficient balance")

    else:
        print("Withdraw amount:", withdraw_amount)

else:
    print("Invalid choice")
    
