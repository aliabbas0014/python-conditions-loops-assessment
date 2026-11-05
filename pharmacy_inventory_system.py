
# Smart Pharmacy Inventory & Sales Management System

print("================================================")
print("     SMART PHARMACY INVENTORY & SALES SYSTEM")
print("================================================")

# Ask how many medicines need to be processed
while True:
    try:
        total_medicines = int(input("Enter number of different medicines: "))

        if total_medicines > 0:
            break
        else:
            print("Please enter at least one medicine.")

    except ValueError:
        print("Please enter a valid whole number.")

# Initialize accumulator and counter
total_revenue = 0
restock_count = 0

# Process each medicine using for loop
for i in range(1, total_medicines + 1):

    print("\nMedicine Number:", i)

    medicine_name = input("Enter medicine name: ").strip()

    # Validate available stock
    while True:
        try:
            stock = int(input("Enter available stock: "))

            if stock >= 0:
                break
            else:
                print("Stock cannot be negative.")

        except ValueError:
            print("Please enter a valid whole number.")

    # Validate price per unit
    while True:
        try:
            price = float(input("Enter price per unit (Rs.): "))

            if price >= 0:
                break
            else:
                print("Price cannot be negative.")

        except ValueError:
            print("Please enter a valid price.")

    # Validate quantity sold
    while True:
        try:
            quantity_sold = int(input("Enter quantity sold: "))

            if quantity_sold >= 0:
                break
            else:
                print("Quantity cannot be negative.")

        except ValueError:
            print("Please enter a valid quantity.")

    # Check stock availability
    if quantity_sold <= stock:

        sales_amount = price * quantity_sold
        remaining_stock = stock - quantity_sold

        # Add sales amount to total revenue
        total_revenue += sales_amount

        print("Sale successful!")
        print("Sales Amount: Rs.", format(sales_amount, ".2f"))

    else:
        remaining_stock = stock

        print("Sale unsuccessful!")
        print("Requested quantity is not available.")
        print("No sales amount added.")

    # Display remaining stock
    print("Remaining Stock:", remaining_stock)

    # Check low stock condition
    if remaining_stock < 10:

        print("WARNING: Low stock! Restocking required.")
        restock_count += 1

# Display final pharmacy report
print("\n================================================")
print("             DAILY PHARMACY REPORT")
print("================================================")

print("Total Medicines Processed:", total_medicines)
print("Total Pharmacy Revenue: Rs.", format(total_revenue, ".2f"))
print("Medicines Requiring Restocking:", restock_count)

print("================================================")
print("          REPORT COMPLETED")
print("================================================")
