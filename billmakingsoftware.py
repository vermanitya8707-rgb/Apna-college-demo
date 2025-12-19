print("===== Welcome to Small Shop Billing =====")

total = 0
bill_details = ""

while True:
    item = input("Enter item name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))

    cost = price * qty
    total += cost

    bill_details += f"{item} - {qty} x {price} = {cost}\n"

    more = input("Add more items? (y/n): ")
    if more.lower() != "y":
        break

print("\n----- BILL -----")
print(bill_details)
print("Total Amount = ₹", total)

# Save bill to file
with open("bills.txt", "a") as file:
    file.write("----- NEW BILL -----\n")
    file.write(bill_details)
    file.write(f"Total = ₹{total}\n\n")

print("Bill saved successfully ✅")