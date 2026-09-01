budget = int(input("What is your budget? "))

score = 0
if budget >= 10000:
    score = score + 3
elif budget >= 5000:  
    score = score + 2
else:
    score = score + 1

print(f"Score: {score}")

company_size = int(input("How many employees does your company have? "))
if company_size >= 50:
    score = score + 3
elif company_size >= 10:
    score = score + 2
else:
    score = score + 1

urgency = input("Is this urgent? yes/no: ")
if urgency == "yes":
    score =  score + 2
else:
    score = score + 0

print(f"Total Score: {score}")

if score >= 7:
    print("This lead is a good lead!")
elif score >= 4:
    print("This lead is a medium lead.")
else:
    print("This lead is not a good lead.")