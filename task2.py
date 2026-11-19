import csv


stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185,
}


def get_portfolio():
    portfolio = {}

    print("Available stocks:", ", ".join(stock_prices))

    while True:
        stock = input("Enter stock symbol (or 'done'): ").strip().upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Unknown stock. Please choose from the available stocks.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: ").strip())
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    return portfolio


def calculate_total(portfolio):
    total = 0

    print("\nStock Portfolio")
    print("Symbol  Quantity  Price  Investment")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = quantity * price
        total += investment
        print(f"{stock:<7} {quantity:<9} ${price:<6} ${investment:.2f}")

    print(f"\nTotal investment value: ${total:.2f}")
    return total


def save_portfolio_csv(portfolio, filename="stock_portfolio.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Investment"])

        total = 0
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = quantity * price
            total += investment
            writer.writerow([stock, quantity, price, f"{investment:.2f}"])

        writer.writerow(["TOTAL", "", "", f"{total:.2f}"])

    print(f"Portfolio saved to {filename}")


if __name__ == "__main__":
    portfolio = get_portfolio()
    calculate_total(portfolio)

    save_choice = input("Save portfolio to CSV? (y/n): ").strip().lower()
    if save_choice == "y":
        save_portfolio_csv(portfolio)
