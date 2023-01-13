# Prices and Cuts:
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for num in prices:
  total_price += num
print(total_price)

average_price = total_price / len(prices)
print("Average Haircut Price: $",average_price)

new_price = [(num - 5) for num in prices]
print(new_price)

# Revenue:

total_revenue = 0

for i in range(0,len(hairstyles)):
 total_revenue += (prices[i] * last_week[i])

print("Total Revenue: $",total_revenue)

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: $",average_daily_revenue)

cuts_under_30 = [ hairstyles[num] for num in range(0,(len(new_price))) if new_price[num] < 30]

print(cuts_under_30)
