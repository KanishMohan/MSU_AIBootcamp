# Create a tuple containing the names of menu sections:
# snacks, meals, drinks, and dessert.

menu_sections = ("snacks", "meals", "drinks", "desserts")

# Print the tuple.
print(f' "The menu items are":, {menu_sections}' )
# Create a list of items for one of the menu sections.
desserts = ["Ice-cream", "Parfait", "Cookie", "Chocolate"]

# Create a list of prices for each of the menu items in the previous list.
dessert_prices = [5.50, 4.25, 2.50, 3.99]


# Ask a user to input a new item and append it to the relevant list.
desserts.append(input("What dessert would you like to add?"))

# Ask a user to input the price of the new item, referenced using list indexing
# and append it to the relevant list.
dessert_prices.append(float(input(f"How much does {desserts[-1]} cost? ")))

# Print the menu and prices.
print(desserts) 
print(dessert_prices)

# Ask the user which item to remove from the menu.
remove_item = input ("Which item would you like to remove?")  

# Find the index of the item and save it as a variable.
index = desserts.index(remove_item)

# Remove the item from the menu list using remove().
desserts.remove(remove_item)

# Remove the item from the prices list using pop().
dessert_prices.pop(index)

# Print the menu and prices again to confirm removal.
print(desserts)
print(dessert_prices)


# Find the most expensive price on the menu.
print(f' "The most expensive dessert is":, {max(dessert_prices)}')

# Find the cheapest price on the menu.
print(f' "The least expensive dessert is":, {min(dessert_prices)}')


# Find the cost if someone bought every item on the menu.
print(f' "The total cost of desserts you bought is":, {sum(dessert_prices)}')

# Confirm that the menu and prices lists are the same length.
print(
    f"The menu lenght is {len(desserts)} and the prices length is "
    + str (len(dessert_prices))
)
