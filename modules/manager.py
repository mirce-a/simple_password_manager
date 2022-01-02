import json
from password_manager import clearscr
import random
import os


# Open database file (database.json) and load contents into dictionary
mode = 'a+' if not os.path.exists('database.json') else 'r'

with open("database.json", mode) as f:
    dbDataRaw = f.read().replace('\n','')
if(dbDataRaw):
    dbData = json.loads(dbDataRaw)
else:
    dbData = {"accounts" : []}

# Write changes to file
def writeToFile():
    # Open db file and write dictionary content
    with open('database.json', 'w') as f:
        f.write(json.dumps(dbData))

def encryptData(data):
    pass

# Show stored accounts
def showAccounts():
    # Iterate through accounts in the JSON file and print key => value
    if (dbData['accounts']):
        for acc in dbData['accounts']:
            print(f"Account ID: {acc['id']}")
            print(f"Account name: {acc['name']}")
            print(f"Username: {acc['username']}")
            print(f"Password: {acc['password']}", end="\n\n")
    else:
        print("Account list empty!")

# Modify an existing account
def modifyAccount():
    if(dbData['accounts']):
        showAccounts()
        c = input("Choose an account to modify (id): ")

        keys = (key for key in dbData['accounts'][int(c)] if key != 'id')

        for field in keys:
            print(f"{field}: {dbData['accounts'][int(c)][field]}")
            while True:
                r = input("Would you like to modify this field? (y/n) ")
                if r.lower() == "y":
                    newData = input("Enter the new value: ")
                    dbData['accounts'][int(c)][field] = newData
                    break
                if r.lower() == "n":
                    break
                else:
                    print("You need to enter a valid answer!")
        clearscr()
        showAccounts()
        writeToFile()
        print("Accounts modified!")
    else:
        print("No accounts to modify!")

# Add a new account
def addAccount():
    newAcc = {}
    if (dbData['accounts']):
        newAcc['id'] = len(dbData['accounts']) + 1
    else:
        newAcc['id'] = 0
    newAcc['name'] = input("Enter a name for the account: ")
    newAcc['username'] = input("Enter username (leave empty if none): ")
    
    while True:
        c = input("Would you like to generate a password? (y/n)")
        if c.lower() == "y":
            newAcc['password'] = generatePassword()
            break
        if c.lower() == "n":
            newAcc['password'] = input("Please enter password(leave empty if none): ")
            break
        else:
            print("You need to enter a valid answer!")
    
    dbData['accounts'].append(newAcc)
    clearscr()
    showAccounts()
    writeToFile()
    print("Added sucessfully!")
    

# Only generate password
def generatePassword():
    password = ""

    dataset = {}
    dataset['letters'] = 'abcdefghijklmnopqrstuvwxyz'
    dataset['lettersUppercase'] = dataset['letters'].upper()
    dataset['digits'] = '1234567890'
    dataset['specialChars'] = '!@#$%^&*()_+=-[{]}\|;:/?.>,<'

    charset = "" + dataset['letters']
    for ds in dataset:
        while True:
            c = input(f"Would you like your password to contain {ds}? (y/n)")
            if c.lower() == "y":
                charset += dataset[ds]
                break
            if c.lower() == "n":
                break
            else:
                print("You need to enter a valid answer!")

    length = int(input("Enter password length: "))

    for i in range(length):
        y = random.choice(charset)
        password += y
    
    return password