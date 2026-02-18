import csv

# Hardcoded stock prices
stock_prices = {
    "APPLE": 180,
    "TSLA": 250,
    "GOOGLE": 2700,
    "MICROSOFT": 300,
    "AMOZON": 3500
}

portfolio = {}
total_investment = 0

print("📈 Advanced Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' to finish.\n")

while True:
    stock_name = input("Enter stock name: ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not available. Try again.\n")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be positive!\n")
            continue
    except ValueError:
        print("Invalid quantity! Enter a number.\n")
        continue

    investment = stock_prices[stock_name] * quantity
    portfolio[stock_name] = {
        "price": stock_prices[stock_name],
        "quantity": quantity,
        "investment": investment
    }

    total_investment += investment
    print(f"✅ Added {stock_name} - Investment: ${investment}\n")

# Display Portfolio Summary
print("\n📊 Portfolio Summary")
print("-" * 40)
for stock, details in portfolio.items():
    print(f"{stock} | Price: ${details['price']} | "
          f"Qty: {details['quantity']} | "
          f"Investment: ${details['investment']}")

print("-" * 40)
print(f"💰 Total Investment Value: ${total_investment}")

# Save to CSV file
with open("portfolio_report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Price", "Quantity", "Investment"])

    for stock, details in portfolio.items():
        writer.writerow([
            stock,
            details["price"],
            details["quantity"],
            details["investment"]
        ])

    writer.writerow([])
    writer.writerow(["Total Investment", "", "", total_investment])

print("📁 Portfolio saved to portfolio_report.csv")
