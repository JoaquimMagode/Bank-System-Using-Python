
class Account:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance is ${self.balance}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance is ${self.balance}."
        else:
            return "Insufficient funds for this withdrawal."

    def get_balance(self):
        return self.balance


class Customer:
    def __init__(self, customer_id, name, address):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.accounts = []

    def create_account(self, account_number, initial_balance=0.0):
        new_account = Account(account_number, initial_balance)
        self.accounts.append(new_account)
        return f"Account {account_number} created for {self.name}."

    def get_account_by_number(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def transfer_money(self, from_customer_id, from_account_number, to_customer_id, to_account_number, amount):
        from_customer = self.get_customer(from_customer_id)
        to_customer = self.get_customer(to_customer_id)

        if from_customer and to_customer:
            from_account = from_customer.get_account_by_number(from_account_number)
            to_account = to_customer.get_account_by_number(to_account_number)

            if from_account and to_account:
                if from_account.get_balance() >= amount:
                    from_account.withdraw(amount)
                    to_account.deposit(amount)
                    return f"Transferred ${amount} from account {from_account.account_number} to account {to_account.account_number}."
                else:
                    return "Insufficient funds for transfer."
            else:
                return "One or both accounts not found."
        else:
            return "One or both customers not found."


# Function to simulate user interaction
def main():
    bank = Bank("Global Bank")
    
    while True:
        print("\nWelcome to Global Bank!")
        print("1. Create Customer Account")
        print("2. Create Bank Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Check Balance")
        print("7. Exit")
        
        choice = input("Please select an option (1-7): ")
        
        if choice == '1':
            customer_id = int(input("Enter Customer ID: "))
            name = input("Enter Customer Name: ")
            address = input("Enter Customer Address: ")
            customer = Customer(customer_id, name, address)
            bank.add_customer(customer)
            print(f"Customer {name} created successfully.")
        
        elif choice == '2':
            customer_id = int(input("Enter Customer ID: "))
            customer = bank.get_customer(customer_id)
            if customer:
                account_number = int(input("Enter Account Number: "))
                initial_balance = float(input("Enter Initial Balance: "))
                print(customer.create_account(account_number, initial_balance))
            else:
                print("Customer not found.")
        
        elif choice == '3':
            customer_id = int(input("Enter Customer ID: "))
            customer = bank.get_customer(customer_id)
            if customer:
                account_number = int(input("Enter Account Number: "))
                account = customer.get_account_by_number(account_number)
                if account:
                    amount = float(input("Enter Deposit Amount: "))
                    print(account.deposit(amount))
                else:
                    print("Account not found.")
            else:
                print("Customer not found.")
        
        elif choice == '4':
            customer_id = int(input("Enter Customer ID: "))
            customer = bank.get_customer(customer_id)
            if customer:
                account_number = int(input("Enter Account Number: "))
                account = customer.get_account_by_number(account_number)
                if account:
                    amount = float(input("Enter Withdrawal Amount: "))
                    print(account.withdraw(amount))
                else:
                    print("Account not found.")
            else:
                print("Customer not found.")
        
        elif choice == '5':
            from_customer_id = int(input("Enter Sender Customer ID: "))
            from_account_number = int(input("Enter Sender Account Number: "))
            to_customer_id = int(input("Enter Recipient Customer ID: "))
            to_account_number = int(input("Enter Recipient Account Number: "))
            amount = float(input("Enter Transfer Amount: "))
            print(bank.transfer_money(from_customer_id, from_account_number, to_customer_id, to_account_number, amount))
        
        elif choice == '6':
            customer_id = int(input("Enter Customer ID: "))
            customer = bank.get_customer(customer_id)
            if customer:
                account_number = int(input("Enter Account Number: "))
                account = customer.get_account_by_number(account_number)
                if account:
                    print(f"Balance for account {account_number}: ${account.get_balance()}")
                else:
                    print("Account not found.")
            else:
                print("Customer not found.")
        
        elif choice == '7':
            print("Thank you for banking with us!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
