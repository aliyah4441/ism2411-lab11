
# ISM2411 - Module 11: Customer Dictionary & Lookup
# Name: Aliyah Fisher

# REFLECTION
# Question 1:
# I would use.get() when working with customer information 
# because some records might have missing details. I would 
# use brackets when I know the information should exist. 
# My rule is to use.get() for data and brackets, for required data.

# Question 2:
# Exercise 8 reminds me of using PivotTables in Excel to
# organize and calculate sales by category.
# Python could be more useful for large datasets because it
# can automatically process information without manually
# updating tables.


# Exercise 1: One Customer
print("Exercise 1:")

customer = {
    "name": "Alice",
    "email": "alice@email.com",
    "tier": "gold",
    "ytd_spend": 1500
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# Exercise 2: Update and Add
print("\nExercise 2:")

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# Exercise 3: Safe Lookup
print("\nExercise 3:")

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: Email does not exist in the dictionary.")


# Exercise 4: Iterate
print("\nExercise 4:")

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only returns dictionary keys.
for key in customer:
    print(key)


# Exercise 5: Lookup Table
print("\nExercise 5:")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount_rate = tier_discounts.get(tier, 0)

price = 200
final_price = price * (1 - discount_rate)

print("Tier:", tier)
print("Discount:", f"{discount_rate * 100:.0f}%")
print("Final Price:", f"${final_price:.2f}")


# Exercise 6: List of Dictionaries
print("\nExercise 6:")

customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]

for person in customers:
    name = person["name"]
    tier = person["tier"]
    rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * rate

    print(f"{name} | Tier: {tier} | Discount: ${discount_amount:.2f}")


# Exercise 7: Nested Catalog
print("\nExercise 7:")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - {details['stock']} remaining")


# Exercise 8: Sales by Region
print("\nExercise 8:")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: ${sales_summary[region]}")
