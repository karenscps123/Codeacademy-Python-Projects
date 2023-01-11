# Sal's Shipping

#  user dialogues
name = input("What is your name?")
print("Hello,", name, "!")
answer = input("What is the weight of your package?")
weight = int(answer)
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
normal_g = cost + 20


# Ground Shipping premium 
print("Normal ground shipping premium cost = $ 125.0 ")
g_prime = 125 

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
drone = cost 

# finding cheapest

if (normal_g < g_prime) and (normal_g < drone):
    smallest_num = normal_g
elif (g_prime < normal_g) and (g_prime < drone):
    smallest_num = g_prime
else:
    smallest_num = drone

print("The cheapest option is : ", smallest_num)
