fruits = ["apple", "banana", "orange"]
fruits1 = fruits.copy() 
fruits1.append("kiwi")
print(fruits1)   # ["apple", "banana", "orange"]

fruits[0] = "mango"
print(fruits)  # ["mango", "banana", "orange"]

# Add items
fruits.append("grape")  
fruits.insert(1, "kiwi")    
print(fruits)  # ["mango", "kiwi", "banana", "orange", "grape"]
# Remove items
fruits.remove("banana")     # Remove by value
last = fruits.pop()        # Remove and return last
del fruits[2]              # Remove by index

print(fruits).strip().sort()