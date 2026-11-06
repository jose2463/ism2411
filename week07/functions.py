# 1. The first bug that was the most easy to spot was the missing : from just over looking the code. I believe I am getting a good understanding on reading code.
# 2. "apply_discount(price, tier)" is applying a discount to the final price depending on its tier. a colleague probably couldn't use it since the body determines the final outcome of the price 
# 3. AI was used on the 5th exercise to help me understand the code that let me to understand what was wrong and be able to fix it.
# --- Exercise 1 ---

# Define calculate tax function

def calculate_tax(price, rate):
        return price * rate

# calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") # 7.50
print(f"Tax on $250 at 8%: ${tax2:.2f}") # 20.00
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}") # 7.50

# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# --- Exercise 3 ---

# Write it out manually first, then refactor into a function

discounted = apply_discount(price, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${after_tax:.2f}")
print(f"After Tax: ${after_tax:.2f}")

# Refracotr into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"final price: ${final_price(price, 'gold', 0.07):.2f}")

# --- Exercise 4 ---

orders = [(200,"gold"), (150,"silver"), (80,"bronze"), (500,"none")]

for price, tier in orders:
     total = final_price(price, tier, 0.07)
     print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# --- Exercise 5 ---

# broken_sales.py - trace and diagnose before fixing anything.

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# --- Exercise 6 ---

x = 100 # apple # Global

def double_it():
    global x
    #x = 999 # another apple (not the same apple as above)
    return x * 2

print(x)
print(double_it())
print(x)
