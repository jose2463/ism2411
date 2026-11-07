# inventory.py
# Author: [Jose]
# Module 10 Lab: Inventory List Manager

print("--- Exercise 1: Build the list ---")

inventory = ["pen", "notebook", "stapler","tape","marker"]
print(inventory)
print(len(inventory))

print("--- Exercise 2: Index Practice  ---")
print(inventory[0]) # first item
print(inventory[-1]) # last item 
middle = len(inventory) // 2
print(inventory[middle]) # middle item

print("--- Exercise 3: Slicing Practice  ---")
print(inventory[:3]) # first three items
print(inventory[-2:]) # last two items
print(inventory[::2]) # every other item

print("--- Exercise 4 : Modifying the list ---")
inventory.append("envelope")
print(inventory) # output: ['pen', 'notebook', 'stapler', 'tape', 'marker', 'envelope']
inventory.remove("tape")
print(inventory)

print("--- Exercise 5: Tuple Comparison  ---")
coords = (40.7128, -74.0060) 

try: 
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates . a location should never change by accident.")

print(coords)

print("--- Exercise 6: Average List of sales  ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

print("--- Exercise 7: Accumulator pattern  ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * .9, 2)) # 10% discount

print("Original prices:", prices)
print("Discounts:", discount)

print("--- Exercise 8: Filter above a threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales)}")


#reflection 1: What surprised me most about how lists work in python: capital letters are more powerful than lowercase4

#reflection 2: A business situation where a python list would have saved me time: