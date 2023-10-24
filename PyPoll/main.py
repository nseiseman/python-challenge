# PyPank Code
# Import the data from the csv files
import os
import csv

# Set path for file
csvpath = os.path.join("Resources/election_data.csv")

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

# Define Variables
total_votes_cast = 0
candidates_and_votes = {} # Use curly brackets to create a dictionary that will store the vote count for each candidate

# Open the dataset in Python to check what the data looks like
# Open and read csv
with open(csvpath, "r") as csvfile:

    # Read the data
    csvreader = csv.reader(csvfile)

    # Skip the header row
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

        # Extract data for the current row
        voter_id = row[0] # Assigns the value of the first column (index 0) to the voter id variable
        county = row[1] # Assigns the value of the second column (index 1) to the county variable
        candidate = row[2] # Assigns the value of the third column (index 2) to the candidate variable

        # Calculate the total number of months included in the dataset
        total_votes_cast = total_votes_cast + 1

        # Create the dictionary that has each candidate and the vote count
        if candidate in candidates_and_votes: # If the candidate is in the dictionary...
            candidates_and_votes[candidate] = candidates_and_votes[candidate] + 1 # Add 1 to the candidates vote count
        else: # If the candidate is not in the dictionary...
            candidates_and_votes[candidate] = 1 # Add the candidate to the dictionary with a count of 1

# Print raw count
print("Election Results")
print(f"Total Votes: {total_votes_cast}")
print("Candidates and Votes (Raw Count)")
print (candidates_and_votes)

# Open new text file to show results
f = open("main.txt", "w")

# Print results
print("Election Results", file=f)
print("--------------------", file=f)
print(f"Total Votes: {total_votes_cast}", file=f)
print("--------------------")

# Iterate through the dictionary to calculate percentage
for candidate, votes in candidates_and_votes.items(): # .item() allows us to iterate through the candidate and votes at the same time
    percentage = (votes / total_votes_cast) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})", file=f) # :.3f used to make value three decimal places

# Print the rest
print("--------------------", file=f)
print("Winner", file=f)