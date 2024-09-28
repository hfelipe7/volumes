# Import the math module in order that I can use math.pi and math.sqrt.
import math 
from datetime import datetime



# this program compute the volume of space inside a tire.
print()
print("Tire Sales and volumen calculator")
print()
# Get the necesary data to calculate the volume.

w = float(input("Enter width of the tire in milimeters: "))
a = float(input("Enter aspect ratio of the tire in inches: "))
d = float(input("Enter diameter of the tire in inches: "))
print()
# calculate the volumen inside the tire.

v = (math.pi * w**2 * (a *(( w*a) + (2540*d))))/10000000000

# datetime
current_day = datetime.now().strftime("%Y-%m-%d")

# store in volumes.txt
with open("volumes.txt", "a") as volumes_file:
     print(f"{current_day}, {w: .0f}, {a: .0f}, {d: .0f}, {v:.2f}", file =volumes_file)
     
# pricing tires
if w == 235 and a == 55 and d == 20:
    price = "$ 323.82"
elif w == 215 and a == 50 and d == 17:
    price = "$ 302.40"
elif w == 245 and a == 45 and d == 18:
    price = "$ 350.0"
elif w== 265 and a == 60 and d == 18:
    price = "$ 352.93"
else:
    price = "Price not available for this tire size."

print(f"Tire price: {price}")
print()
print(f"the volume of the tire is: {v:.2f} liters")

# Ask user if she desires wants to buy tires with the dimensions she entered.
buy_tires= input("Would you like to buy tires with these dimensions? (yes/no): ")

if buy_tires == "yes":
    phone_number =  input("Please enter your phone number: '1234567890': ")
    #formatting id number and phone number
    formatted_phone_number = f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number [6:]}"  
    with open("volumes.txt", "a") as volumes_file:
     print(f"Client phone number: {formatted_phone_number}", file =volumes_file)
     print("------------------------------------", file=volumes_file)
else:
    with open("volumes.txt", "a") as volumes_file:
        print("------------------------------------", file=volumes_file)



#conclusion
print("Data has been written to volumes.txt" )
print()
#



