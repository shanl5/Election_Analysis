# As denoted in Module 3.4.4 : "Add our dependencies"...
# From Module 3.4.2 -
import csv
# From Module 3.4.2 - open a module that allows interaction with the operating system...
import os

# Module 3.4.4 description: "Assign a variable to load a file from a path." ...
# Assign a variable for the file to load and the path.
#x. 
#    file_to_load = 'Resources\election_results.csv'
#-x.
file_to_load = os.path.join("Resources","election_results.csv")

# Module 3.4.4 description: "Assign a variable to save the file to a path." ...
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Module 3.5.1 (1)/(3) : Initialize a total vote counter.
total_votes = 0

# Module 3.5.2 (1)/(4) : Declare a new list."
candidate_options = []

# Module 3.5.3 (a) : Declare new dictionary to tally votes for each candidate..
# key is each candidate's name, value for key is vote count for that candidate"
# so like this - {"candidate_name1": votes, "candidate_name1": votes, "candidate_name3": votes}
candidate_votes = {}

# Module 3.5.5 Determine the winning candidate (I)/(III)
# ` Declare a variable that holds an empty string value for the winning candidate
# ` Declare a variable for the "winning count" equal to zero
# ` Declare a variable for the "winning_percentage" equal to zero
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
#x0a.NO LONGER USING THIS...
#   election_data = open(file_to_load, 'r')
#-x0a.
with open(file_to_load) as election_data:
    
    # Module 3.4.4 : "To do: read and analyze the data here."
    # To do: perform analysis.
    #xx2. Replace test print with analysis steps.
    #   print(election_data)
    #-xx2.

    # Module 3.4.4 : one comment and one code line below...
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # As described in Module 3.4.4 -
    #  ' The variable, file_reader, is referencing the file object, which is
    #  ' stored in memory. To "pull" the data out of the file object, we can
    #  ' iterate through the file_reader variable and print each row, including
    #  ' the headers, or column names.
    #  '
    # In the module, instruction is given to -
    #  ' Add the following code to (this program module) and
    #  ' run the file in the VS Code terminal.
    #  '

    # Module 3.4.4 - confirm that "we skipped the header row" ...
    #cc. Adjust comment to reflect 'removed' code...
    #   # Read and print the header row.
    # Comment ^^^above^^^ becomes the comment below...
    # Read the header row.
    headers = next(file_reader)
    #   print(headers)
    #-cc.

    # # Print each row in the CSV file.
    for row in file_reader:
        #   print(row)
        # Module 3.5.1 (2)/(3) : Add to the total vote count.
        total_votes += 1

        # Module 3.5.2 (2)/(4) : Get the candidate's name (3rd column is index 2).
        candidate_name = row[2]
        # Module 3.5.2 (3)/(4) : .. and add the name to the list of candidates.
        if not(candidate_name in candidate_options):
            candidate_options.append(candidate_name)
            
            # Module 3.5.3 (b) : Begin tracking the candidate's vote count...
            candidate_votes[candidate_name] = 0

        # Module 3.5.3 (c) : Increment votes for candidate name
        candidate_votes[candidate_name] += 1

# Module 3.5.4 :
# ' Determine the percentage of votes for each candidate by looping through the counts.
# ' (i) Iterate through the candidate list.
for candidate_name in candidate_votes:

    # ' (ii) Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    
    # ' (iii) Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # ' (iv) Print the candidate name and percentage of votes.
    print(f"{candidate_name}:  {vote_percentage:.1f}% ({votes:,})\n")

    # Module 3.5.5 Determine the winning candidate (II)/(III)
    # 1st - Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):

        # 2nd - If true then set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage

        # 3rd - Set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name

# Module 3.5.5 Determine the winning candidate (III)/(III)
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------\n"
)
print(winning_candidate_summary)

#.#.#   
#.#.#   # Module 3.5.1 (3)/(3) : Print the total votes.
#.#.#   print(total_votes)
#.#.#   
#.#.#   # Module 3.5.2 (4)/(4) : Print the list of (unique) candidate names."
#.#.#   #xM3.5.2. The code for this can be made more compact, listing in a single line
#.#.#   #   for i in range(len(candidate_options)):
#.#.#   #       print(f"{candidate_options[i]}\n")
#.#.#   #-xM3.5.2.
#.#.#   print(candidate_options)
#.#.#   
#.#.#   # Module 3.5.3 (d) : Print the candidate vote dictionary.
#.#.#   print(candidate_votes)
#.#.#   
#.#.#   # Using the open() function with the "w" mode we will write data to the file.
#.#.#   #x1a.
#.#.#   #   open(file_to_save, "w")
#.#.#   #-x1a.
#.#.#   #
#.#.#   #x1b. Will use with statement instead
#.#.#   #   # Use the open statement to open the file as a text file.
#.#.#   #   outfile = open(file_to_save, "w")
#.#.#   #-x1b.
#.#.#   #
#.#.#   # Using the with statement open the file as a text file.
#.#.#   with open(file_to_save, "w") as txt_file:
#.#.#   #
#.#.#       # Write some data to the file.
#.#.#       #xx. In place of "Hello World," add to the file counties "Arapahoe," "Denver," and "Jefferson"
#.#.#       #   txt_file.write("Hello World")
#.#.#       #-xx.
#.#.#       #xx1. Will use Method one but instead separate counties with '\n' (newline) character 
#.#.#       #   # Method one - one line for each county (remember to add separating comma and space)
#.#.#       #   txt_file.write("Arapahoe, ")
#.#.#       #   txt_file.write("Denver, ")
#.#.#       #   txt_file.write("Jefferson")
#.#.#       #-xx1.
#.#.#       #
#.#.#       # In the output file - above the counties (that are written with chosen Method) - write out a header
#.#.#       hdr = "Counties in the Election\n"
#.#.#       txt_file.write(hdr)
#.#.#       # Underline the heading with dashes ...
#.#.#       for i in range(len(hdr)):
#.#.#           txt_file.write("-")
#.#.#       txt_file.write("\n")
#.#.#       #
#.#.#       # Method one (revisited) - one line for each county (separating with '\n')
#.#.#       txt_file.write("Arapahoe\n")
#.#.#       txt_file.write("Denver\n")
#.#.#       txt_file.write("Jefferson")
#.#.#       
#.#.#       #xx0. Try Method one above
#.#.#       #   # Method two = the three counties in one line (separated by comma and space)
#.#.#       #   txt_file.write("Arapahoe, Denver, Jefferson")
#.#.#       #-xx0.
#.#.#   
#.#.#   #x1d. Will use with statement instead
#.#.#   #   # Write some data to the file.
#.#.#   #   outfile.write("Hello World")
#.#.#   #-x1d.
#.#.#   #
#.#.#   
#.#.#   #x1c. Will use with statement instead
#.#.#   #   # Close the file
#.#.#   #   outfile.close()
#.#.#   #-x1c.
#.#.#   
#.#.#   #x0b.NO LONGER USING THIS...
#.#.#   #   # Close the file.
#.#.#   #   election_data.close()
#.#.#   #-x0b.
#.#.#   
#.#.#   # Check if all complete?
#.#.#   # The data we need to retrieve.
#.#.#   # 1. The total number of votes cast
#.#.#   # 2. A complete list of candidates who received votes
#.#.#   # 3. The percentage of votes each candidate won
#.#.#   # 4. The total number of votes each candidate won
#.#.#   # 5. The winner of the election based on popular vote.
#.#.#   #
