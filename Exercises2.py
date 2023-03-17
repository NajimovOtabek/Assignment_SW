# Given Inputs
def inputs():
    cover_price = 24.95
    discount = 0.4
    shipping_first = 3
    shipping_additional = 0.75
    num_copies = 60
    return cover_price, discount, shipping_first, shipping_additional, num_copies

# Calling the values
cover_price, discount, shipping_first, shipping_additional, num_copies = inputs()

# Calculations
discounted_price = cover_price * (1 - discount)  # Calculate the discounted price
total_shipping_cost = shipping_first + (num_copies - 1) * shipping_additional  # Calculate the total shipping cost
total_cost = discounted_price * num_copies + total_shipping_cost  # Calculate the total cost

# Print the result
total_cost = round(total_cost, 2)
print(f"The total wholesale cost for {num_copies} copies is ${total_cost}")