# PyBank Code
# Import the data from the csv files
import os
import csv

# Set path for file
csvpath = os.path.join("Resources/budget_data.csv")

# ----------

# Open the dataset in Python to check what the data looks like
# Open and read csv
with open(csvpath, "r") as csvfile:

    # Read the data
    csvreader = csv.reader(csvfile)

    #Process the data in each row
    for row in csvreader:
        print(row)

# ----------

# Define variables to store data
total_months = 0 # Keeps track of total months in dataset. Starts at O and increases as you loop through the data
total_profit_or_loss = 0 # Keeps track of total profit/loss in dataset. Starts at 0 and increases as you loop through the data
previous_profit_or_loss = 0 # Used to calculate the change in profit/loss from line to line. Start at 0 and increases or decreases as you loop through the data 
change_in_profit_or_loss = [] # An empty list that will be filled in the changes in profit/loss from month to month. Uses to calculate the average change
months = [] # An empty list that will be filled with the months. Used to match up with the changes in profit/loss

# Open and read csv
with open(csvpath, "r") as csvfile:

    # Read the data
    csvreader = csv.reader(csvfile)

    # Skip the header row
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

        # Extract data for the current row
        month = row[0] # Assigns the value of the first column (index 0) to the month variable
        profit_or_loss = int(row[1]) # Assigns the value of the second column (index 1) to the profit/loss variable

        # Calculate the total number of months included in the dataset
        total_months = total_months + 1

        #Calculate net toal profit/loss included in the dataset
        total_profit_or_loss = total_profit_or_loss + profit_or_loss

        # Calculate the change in profit/loss
        if total_months > 1: # Starts at the second month (index 1) because if it started at the first (index 0) there would be no previous profit/loss
            change = profit_or_loss - previous_profit_or_loss
            change_in_profit_or_loss.append(change)
            months.append(month)
        
        # Update the previous profit/loss for the next iteration
        previous_profit_or_loss = profit_or_loss
    
# Calculate the average change in profit/loss
average_change = sum(change_in_profit_or_loss) / (total_months - 1) # Need to subtract by 1 because row starts at 0 

# Find the greatest increase and decrease in profit/loss
max_increase = max(change_in_profit_or_loss)
max_decrease = min(change_in_profit_or_loss)

# Find the corresponding months for the increase and decrease
max_increase_month = months[change_in_profit_or_loss.index(max_increase)] # Finds the index of the max increase value within the list. Then finds the corresponding month to the max position
max_decrease_month = months[change_in_profit_or_loss.index(max_decrease)] # Uses same logic as above but for the max decrease

# Open new text file to show results
f = open("main.txt", "w")

# Print the results
print("Financial Analysis", file=f)
print("----------", file=f)
print(f"Total Months: {total_months}", file=f) # Use f string to allow for variables or functions to be printed
print(f"Total Profit/Loss: ${total_profit_or_loss}", file=f) # Use curly brackets to insert the variables or formulas
print(f"Average Change: ${average_change:.2f}", file=f) # :.2f used to make value two decimal places
print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})", file=f)
print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})", file=f)

# ----------