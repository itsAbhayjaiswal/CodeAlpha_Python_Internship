# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180,
    "NVDA": 120
}

portfolio = {}

print("=" * 50)
print("        STOCK PORTFOLIO TRACKER")
print("=" * 50)

print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter 'done' when you have finished adding stocks.")

while True:

    stock = input("\nEnter stock symbol: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity


# Calculate total investment
total_investment = 0

print("\n" + "=" * 50)
print("             PORTFOLIO")
print("=" * 50)

report = []

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    line = f"{stock}: {quantity} shares × ${price} = ${investment}"

    print(line)
    report.append(line)

print("-" * 50)

print(f"TOTAL INVESTMENT: ${total_investment}")

report.append("-" * 50)
report.append(f"TOTAL INVESTMENT: ${total_investment}")


# Save report
with open("portfolio_report.txt", "w") as file:

    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("=" * 40 + "\n")

    for line in report:
        file.write(line + "\n")

print("\nReport saved as portfolio_report.txt")