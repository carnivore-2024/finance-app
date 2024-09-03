# Function to read item data from a file and populate lists
def items(item, costPrice, sellingPrice):
    # Open the file 'items.txt' in read mode
    with open("items.txt", "r") as f:
        # Iterate over each line in the file
        for line in f:
            # Find the position of '#' and '@' in the line
            position = line.rfind('#')
            position2 = line.rfind("@")
            # Append the item name (text before '#') to the 'item' list
            item.append(line[:position])
            # Append the cost price (text between '#' and '@') to the 'costPrice' list, converted to float
            costPrice.append(float(line[position+1: position2]))
            # Append the selling price (text after '@', stripped of newline) to the 'sellingPrice' list, converted to float
            sellingPrice.append(float(line[position2+1:].strip("\n")))

# Main function to handle user interaction and calculations
def main():
    # Initialize empty lists for items, cost prices, and selling prices
    item = []
    costPrice = []
    sellingPrice = []

    # Call the 'items' function to populate the lists with data from the file
    items(item, costPrice, sellingPrice)
    
    # Initialize an empty list for the number of items sold and other variables
    itemSold = []
    n = len(item)  # Number of different items

    # Fixed rent cost
    rent = 25000
    # Initialize variables for total calculations
    totalIncome = 0
    totalSellingPrice = 0
    TotalCostPrice = 0
    totalItemSold = 0
    income = []

    # Iterate over each item to get user input and calculate totals
    for i in range(n):
        # Ask user how many of the current item they have sold
        itemSold.append(int(input(f"Enter how many {item[i]} you have sold!: ")))
        # Update total item sold
        totalItemSold += itemSold[i]
        # Calculate total income for the current item
        total = sellingPrice[i] * itemSold[i]
        # Append the total income to the 'income' list
        income.append(total)
        # Print the income from selling the current item
        print(f"You made R{income[i]:.2f} from selling {item[i]}")
        # Update overall totals
        totalIncome += total
        totalSellingPrice += sellingPrice[i] * itemSold[i]
        TotalCostPrice += costPrice[i] * itemSold[i]
    
    # Check if the total selling price equals the total cost price
    if totalSellingPrice == TotalCostPrice:
        print("The total selling price equals the total cost price. Break-even calculation is not possible.")
        return
    
    # Calculate the break-even point in terms of number of items
    breakEvenPointItems = rent / (totalSellingPrice - TotalCostPrice)
    # Calculate the break-even point in terms of money
    breakEvenPointMoney = rent
    
    # Calculate the average number of items sold
    avg = totalItemSold / n
    
    # Compare average items sold to break-even point and print the result
    if avg > breakEvenPointItems:
        print(f"You exceeded the break-even point by {avg - breakEvenPointItems:.2f} items or R{totalIncome - breakEvenPointMoney:.2f}")
    elif avg == breakEvenPointItems:
        print(f"You are at the break-even point. You have made R{totalIncome:.2f}, which covers the break-even point of R{breakEvenPointMoney:.2f}")
    else:
        print(f"You are below the break-even point. You need to sell {breakEvenPointItems - avg:.2f} more items or generate an additional R{breakEvenPointMoney - totalIncome:.2f}")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
