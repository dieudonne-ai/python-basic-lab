#in this file you find also some statment for data manipulation

person = {"name": "Alice", "age": 30}

# Add or update
person["email"] = "alice@email.com"  # Add new
person["age"] = 31                   # Update existing

print(person)
# Remove items
#del person["email"]              # Remove by key
#age = person.pop("age")          # Remove and return
#person.clear()                   # Remove all items
