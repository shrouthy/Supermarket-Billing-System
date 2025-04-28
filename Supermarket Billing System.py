#Supermarket Billing System

print("-"*50)
print("Welcome to Supermarket Billing System")
print("-"*50)

#Ask for customer details
Name = input("Enter your name: ")
Phone = input("Enter your phone number: ")

#dictionary of products and their price
products = {"Milk": 30.0,"Banana": 20.0,"Chocolate": 35.0,"Flour": 27.0,"Rice": 50.0,"Sugar": 25.0,"Paneer": 80.0,"Yogurt": 20.0,"Chips": 10.0,"Tea": 50.0,
"Coffee": 70.0,"Juices": 20.0,"Apple": 50.0,"Cooking oil":60.0,"Ghee": 250.0,"Grapes": 30.0,"Tomatoes": 40.0,"Potatoes": 30.0,"Biscuits": 10.0}

print("-"*50)
print("Items in stock:")
print("-"*50)

for i,j in products.items(): #to show all the items in products
    print(i,":",j) #tuple unpacking
print("-"*50)

while True:
    amount = 0
    total = 0
    purchased_items = [] #List to store purchased item's details

    while True:
        p_item = input("Enter the product name: ").title()
        if p_item not in products:
            print("Product not found. Please Enter a valid item.")
            continue
        quantity = float(input("Enter the quantity: "))
        price = products[p_item]
        item_total = price * quantity
        purchased_items.append([p_item, quantity, price, item_total]) #Add item details to bill
        amount += item_total

        repeat = input("Add another item? (yes/no): ")
        if repeat == "no":
            break

    #calculate discount based on total amount
    if amount > 5000:
            discount = 0.25
            percent = "25% discount applied"
    elif amount > 3500:
        discount = 0.20
        percent = "20% discount applied"
    elif amount > 1500:
        discount = 0.15
        percent = "15% discount applied"
    elif amount > 500:
        discount = 0.10
        percent = "10% discount applied"
    else:
        discount = 0.05
        percent = "5% discount applied"

    total = amount - (amount*discount)
    
    #Formatting the receipt
    print("\n" + "-"*23 + "BILL" + "-"*23)
    print("Name:",Name)
    print("Phone number:",Phone)
    print("-"*50)
    print(f"{'Product':<15}{'Qty':<10}{'Price':<10}{'Total':<10}") #Receipt header with spacing
    print("-"*50)
    for item in purchased_items:
        print(f"{item[0]:<15}{item[1]:<10}{item[2]:<10}{item[3]:<10}") #Itemized bill
    print("-"*50)
    print("Thank you for shopping with us!")

    again = input("Do you want to process another bill? (yes/no): ").lower()
    if again == "no":
        break