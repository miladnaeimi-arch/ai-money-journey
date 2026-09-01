name = input("What's your name? ")
age = int(input("How old are you? "))
age_in_10_years = age+10
city = input("what city do you live in?")
year_born = int(input("What year were you born?"))
old_2050 = 2050-year_born

print(f"Hello {name}!")
print(f"You are {age} years old.")
print(f"In 2050, you will be {old_2050} years old.")
print(f"In 10 years, you will be {age_in_10_years} years old.")
print (f"Hello {name}! You are {age} years old and you live in {city}.")

if age >=18:
 print(f"you_are_an_adult.")

else:
 print(f"you_are_under_18.")
