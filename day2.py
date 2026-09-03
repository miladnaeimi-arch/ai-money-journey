customers = ["Alex", "Sara", "John"]

print(customers)
print(customers[0])
print(customers[1])
print(customers[2])
for customer in customers:
    print(customer)
for customer in customers:
    print(f"Sending email to {customer}")
customer = {
    "name": "Alex",
    "budget": 12000,
    "company_size": 60,
    "urgent": True
}

print(customer)
print(customer["name"])
print(customer["budget"])
print(customer["company_size"])
print(customer["urgent"])
customers = [
    {
        "name": "Alex",
        "budget": 12000,
        "company_size": 60,
        "urgent": True
    },
    {
        "name": "Sara",
        "budget": 6000,
        "company_size": 20,
        "urgent": False
    },
    {
        "name": "John",
        "budget": 2000,
        "company_size": 5,
        "urgent": True
    }
]
def check_customer(customer):
    print(f"Checking {customer['name']}...")
    print(f"Budget: ${customer['budget']}")
for customer in customers:
        check_customer(customer)