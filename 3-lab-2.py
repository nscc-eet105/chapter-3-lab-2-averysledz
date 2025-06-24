#Avery Sledz
#Lab 3-lab-2
#6-23-25
print ("jane's Stuff Store")
print("")
num_items = int(input("How many items would you like to purchase? "))
print("")
total_cost = 0
for i in range(num_items) :
    price = float(input(f'Enter the price of item {i + 1}: '))
    total_cost = total_cost + price
print("")
average = total_cost / num_items
print (f"The total cost of your items is ${total_cost:.2f}")
print (f"The average cost of each item is ${average:.2f}")
