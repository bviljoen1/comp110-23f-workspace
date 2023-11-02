"""Practice with dictionary syntax"""
__author__ = "730579443"

# Create a new dictionary
ice_cream: dict[str,int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Create my Dictionary")

#Adding a key,value pair to a dictionary
ice_cream["mint"] = 3
print("Added mint to dictionary:")
print(ice_cream)

ice_cream.pop("mint")
print("Mint has been removed from dictionary:")
print(ice_cream)

# Accessing a value at certain key
print(f"There are {ice_cream['chocolate']} orders of chocolate ice cream")

# Updating a value at a certain key
ice_cream["vanilla"] = 10

print(f"The updated Dictionary is: {ice_cream}")


# Print the length
print(f"There are {len(ice_cream)} key-value pairs in dictionary")

# if mint and chocolate are in ice cream
if "mint" in ice_cream:
    print(f"There are {ice_cream['mint']} orders of mint!")
else:
    print(f"No orders of mint")

if "chocolate" in ice_cream:
    print(f"There are {ice_cream['chocolate']} orders of chocolate!")
else:
    print("No orders of chocolate")

print("Chocolate in dictionary?")
print("chocolate" in ice_cream)

print("Mint in dictionary?")
print("mint" in ice_cream)

# using "in" in a conditional6.
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("No orders of mint")


# Using For loops for this shit. loop through dictionary and print out each flavor and num of orders
for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders!")
