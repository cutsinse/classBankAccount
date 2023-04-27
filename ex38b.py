#Ex 38b: Study Drills
#I used ChatGPT to explain what a class is, and then gave me a task. 
from sys import exit

class BankAccount:
	def __init__(self, name, balance):
		#the "self" is required, because the name of the function (__init__ in this case) is also used as an argument
		#see ex38 for more details. 
		self.name = name
		self.balance = balance
		
	def withdraw(self, amount):
		self.balance = self.balance - amount
		print(self.balance)
		
	def deposit(self, amount):
		self.balance = self.balance + amount
		print(self.balance)
	
	def get_balance(self):
		print(self.balance)

#program flow starts here
print("Welcome to the Bank of Mew!")	

name = input("What is your name? ")
start_balance = int(input("What is your starting balance? "))

user_account = BankAccount(name, start_balance)

print(f"Ok, so you are {user_account.name}, and your starting balance is {user_account.balance}") 

while True:
	print("What do you want to do now?  You can withdraw, deposit, or get balance.")
	choice = input(">")
	if "withdraw" in choice:
		amount = int(input("How much? "))
		user_account.withdraw(amount)
	elif "deposit" in choice:
		amount = int(input("How much? "))
		user_account.deposit(amount)
	elif "get" in choice or "balance" in choice:
		user_account.get_balance()
	elif "quit" in choice:
		print("Goodbye!")
		exit(0)
	else:
		print("Error, try again")
		


