print("Welcome to the age calculating program: ")
#Take the input of age from user 
age = input("What is your current age?")
#Convert the data type of age to integer from string
Age = int(age)
#calculate the left days from total days if you live 100 years
Days = (36500 - Age*365)
#calculate the left weeks from total weeks if you live 100 years
Weeks = (5200 - Age*52)
#calculate the left months from total months if you live 100 years
Months = (1200 - Age*12)
#printing the value of how many days, months, and weeks are left if you live 100 years.
#Leap year is negoatiable
print(f"You have {Days} days, {Weeks} weeks,{Months} months left if you live 100 years. ")
