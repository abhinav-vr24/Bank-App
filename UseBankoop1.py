import pickle
import os
from Bankoop1 import *

FILE_NAME = "bank.dat"


def load_holders():
    """Load holders from the binary file."""
    if os.path.exists(FILE_NAME):   # Check Does File exits or not?
        with open(FILE_NAME, "rb") as file1:
            return pickle.load(file1)
    return []


def save_holders(holders):
    """Save holders to the binary file."""
    with open(FILE_NAME, "wb") as file1:
        pickle.dump(holders, file1)


all_holders = []
hol01 = holder()
hol02 = holder()
all_holders.append(hol01)
all_holders.append(hol02)


bnk01 = Bank(all_holders)


#try:
    #hol01 = holder()
    #hol02 = holder()
    #all_holders.append(hol01)
    #all_holders.append(hol02)
    
    #choice = input(""" 1. Saving Account, 2. Current Account, Enter Choice :""")

    #if choice == "1":
        #account = Saving_Account(hol01)
    #elif choice == "2":
        #account = Current_Account(hol01)
    #else:
        #raise ValueError("Invalid Choice")


    #print(account.Show_Bank_Detail())
    #account.deposit()
    #account.withdraw()


    #if isinstance(account, Saving_Account):
        #print(account.Saving_Current_Balance())
    #else:
        #print(account.C_Current_Balance())

#except ValueError as e:
    #print("Value Error :", e)
#except Exception as e:
    #print("Unexpected Error :", e)
#finally:
    #print("\nThank you for banking with us.")



# Save holders to the binary file.
save_holders(all_holders)

# Load holders from the binary file
all_holders = load_holders()

print(all_holders[0])
print(all_holders[1])

