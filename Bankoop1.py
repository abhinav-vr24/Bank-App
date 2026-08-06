class Bank:
    account_no = 100000001  # Fixing 1st value of Account No

    def __init__(self, holder):
        self.acc_no = Bank.account_no
        Bank.account_no += 1

        self.holder = holder
        self.__bal = 0    # Private Attribute 
        self.last_deposit = 0
        self.last_withdraw = 0


    def get_balance(self):
        return self.__bal


    # Check Withdraw Condition (Setter)
    def withdraw(self):
        temp = int(input("Enter Your Withdraw Amount:"))

        if temp > self.__bal:
            raise ValueError("Your Bank Balance is low")
        else:
            self.__bal -= temp
            self.last_withdraw = temp
            print("Successful Withdraw")
        return temp

        

    # Check Min Deposite Amount >= 0 (Setter)
    def deposite(self):
        temp = int(input("Enter Your Deposite Amount"))

        if temp < 0 :
            raise ValueError("Deposite Amount can not be -ve")
        else:
            self.__bal += temp
            self.last_deposit = temp
            print("Successful Deposite")
        return temp

        

    # Showing All the Bank details
    def Show_Bank_Detail(self):
        return ("Account_No:", self.acc_no,
            "Balance:", self.get_balance(),
            "Holder:", self.holder.show_holder_details())






# Creating the Saving Account Class under Bank Class
class Saving_Account(Bank):

    def __init__(self, holder):
        super().__init__(holder)
        self.minbal = 1000
        # Initialize with minimum balance
        self._Bank__bal = self.minbal  
        holder.saving = self


    # Overriding deposit method
    def deposit(self):
        temp = int(input("Enter Your Deposit Amount: "))

        if temp < 0:
            raise ValueError("Deposit Amount cannot be negative")
        else:
            self._Bank__bal += temp
            self.last_deposit = temp
            print("Successful Deposit")
        return temp



    # Overriding withdraw method
    def withdraw(self):
        temp = int(input("Enter Your Withdraw Amount: "))

        if temp <= 0:
            raise ValueError("Withdraw amount must be positive")

        # Ensure balance never goes below minbal
        if (self._Bank__bal - temp) < self.minbal:
            raise ValueError(f"Withdrawal denied. Minimum balance of {self.minbal} must be maintained.")
        else:
            self._Bank__bal -= temp
            self.last_withdraw = temp
            print("Successful Withdraw")
        return temp



    def set_minbal(self, change_min_bal):
        self.change_min_bal = change_min_bal
        return change_min_bal




    def Show_Saving_Account_Details(self):
        return (
            "Account_No:", self.acc_no,
            "Account_Holder:", self.holder.show_holder_details(),
            "Deposit Amount:", self.last_deposit,
            "Withdraw Amount:", self.last_withdraw,
            "Current Balance:", self.get_balance())

    

    def Saving_Current_Balance(self):
        return "Your Saving Account Balance is:", self.get_balance()





# Create Current Class under Bank Class
class Current_Account(Bank):

    def __init__(self, holder, overdraft=1000):
        super().__init__(holder)
        self.overdraft = overdraft
        self._Bank__bal += self.overdraft

        holder.current = self

    # Show Methods
    def Show_Current_Account_Details(self):
        return (
            "Account_No:", self.acc_no,
            "Account_Holder:", self.holder.show_holder_details(),
            "Overdraft_Capital:", self.overdraft,
            "Deposite Amount:", self.last_deposit,
            "Withdraw Amount:", self.last_withdraw,
            "Current Balance:", self.get_balance())


    def C_Current_Balance(self):
        return "Your Current Account Balance is:", self.get_balance()








# Holder Class
class holder:
    holderid = 1000001

    def __init__(self):
        self.holdnam = self.get_holder_name()
        self.address = self.get_address()
        self.holdid = holder.holderid
        holder.holderid += 1

      # Accounts of this holder
        self.saving = None
        self.current = None

        self.show_holder_details()
        self.show_address_details()



    def get_holder_name(self):
        temp = input("Enter Holder Name: ")

        if len(temp) == 0:
            raise ValueError("Holder name cannot be empty")
        return temp

    

    def get_address(self):
        temp = input("Enter Address: ").strip()

        if len(temp) == 0:
            raise ValueError("Address cannot be empty")
        return temp



    def show_address_details(self):
        return self.address



    def show_holder_details(self):
        return (
            "holder id:", self.holdid,
            "holder name:", self.holdnam,
            "holder Address:", self.show_address_details())



