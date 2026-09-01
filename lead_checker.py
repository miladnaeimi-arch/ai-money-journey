budget = int(input("What is your budget? "))

company_size = int(input("How many employees does your company have? "))

urgency = input("Is this urgent? yes/no: ")

score = 0
if budget >= 10000:
    score = score + 3
elif budget >= 5000:  
    score = score + 2
else:
    score = score + 1

print(f"Score: {score}")