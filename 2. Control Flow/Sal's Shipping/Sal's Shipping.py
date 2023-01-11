# Sal's Shipping

weight = 8.4
cost = 0

# Ground Shipping 
if weight <= 2:
  cost = weight * 1.50
elif (weight > 2 and weight <= 6):
  cost = weight * 3.0
elif (weight > 6 and weight <= 10):
  cost = weight * 4.0
else:
  cost = weight * 4.75
print("Normal ground shipping cost = $", cost + 20)

# Ground Shipping premium 
print("Normal ground shipping premium cost = $ 125.0 ")

# Drone shipping
if weight <= 2:
  cost = weight * 4.5
elif (weight > 2 and weight <= 6):
  cost = weight * 9.0
elif (weight > 6 and weight <= 10):
  cost = weight * 12.0
else:
  cost = weight * 14.25
print("Drone shipping cost = $", cost)
