print("Hello World" + "!")

msg = "this is on one line"
print(msg)

msg2 = "this prints on...\n\r...two lines.\n"
print(msg2)
print("this also prints\n on two lines")

# Lists of Dictionaries
# First, create an empty list called voting_data
voting_data = []
#
# Then add, or append, each dictionary to the voting_data list with the following code and press Enter:
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
#
# When we type voting_data and press Enter, we get the following output:
print(f"\nThis is the output from voting_data: \n", voting_data)
#
# We can use list methods to:
# 1. Get the length of the voting_data list of dictionaries.
print(f"\n1. Get the length of the voting_data list of dictionaries using len(voting_data) ... ", \
    len(voting_data),"\n")
#
# 2. Use indexing and slicing to get one or more dictionaries:
print(f"\nvoting_data[-1:] outputs this ... {voting_data[-1:]}\n")
#
print(f"\nvoting_data[:-1] outputs this ... {voting_data[:-1]}\n")
#
print(f"\nThe output from voting_data[:] is:\n{voting_data[:]}")
#
print(f"\nThe output from voting_data[0:0] is:\n {voting_data[0:0]}")
#
print(f"\nThe output from voting_data[1:3] is:\n {voting_data[1:3]}")
#
print(f"\nThe output from voting_data[0:-2] is:\n {voting_data[0:-2]}")
#
print(f"\nThe output from voting_data[0:-1] is:\n {voting_data[0:-1]}")
#
# # 3. Use the append(), insert() and remove() methods to add and remove
#    one or more dictionaries.
voting_data.append({"county":"Arapahoe", "registered_voters":422829})
msg_to_print = 'voting_data.append({"county":"Arapahoe","registered_voters":422829})\n'
#print(f"voting_data after voting_data.append({'county':'Arapahoe','registered_voters':422829}):\n", voting_data)
print(f'\nvoting_data after ' + msg_to_print, f'is: \n', voting_data)
#
voting_data.insert(2, {"county":"Arapahoe", "registered_voters":422829})
#print(f'...and after voting_data.insert(2, {"county":"Arapahoe", "registered_voters":422829}):\n'voting_data)
print('\n...and after voting_data.insert(2, {"county":"Arapahoe", "registered_voters":422829}):\n')
voting_data
#
voting_data.remove({"county":"Arapahoe", "registered_voters":422829})
#print(f'-next after voting_data.remove({"county":"Arapahoe", "registered_voters":422829}):\n', voting_data)
print('\n-next after voting_data.remove({"county":"Arapahoe", "registered_voters":422829}):\n')
voting_data
#
voting_data.remove({"county":"Arapahoe", "registered_voters":422829})
#print(f'-now after second voting_data.remove({"county":"Arapahoe", "registered_voters":422829}):\n', voting_data)
print('\n-now after second voting_data.remove({"county":"Arapahoe", "registered_voters":422829}):\n')
voting_data
#
# 4. Change a value for one of the keys in the list of dictionaries.
voting_data[1]["county"] = "El Paso"
print(f'\nHave changed like this: voting_data[1]["county"] = "El Paso" and result is:\n', voting_data)
#

# create empty list called voting_data_delftstack
voting_data_delftstack=[]

# add each dictionary (three of them) to the voting_data_delftstack list
voting_data_delftstack.append({"county":"Arapahoe","registered_voters":422829})
voting_data_delftstack.append({"county":"Denver","registered_voters":463353})
voting_data_delftstack.append({"county":"Jefferson","registered_voters":432438})

# output voting_data_delftstack list
print(f"\nThis result:\n", voting_data_delftstack, "is the output of voting_data_delftstack")
print(f"\nThis result:\n", voting_data_delftstack[0:0], "is the output of voting_data_delftstack[0:0]")

# output empty list
print(f"\nThis result:\n", voting_data_delftstack[:], "is the output of voting_data_delftstack[:]")

# Module 3.2.7 (1) Add new county "El Paso" and its registered voters, 461149, to the
# second position in voting_data_delftstack
voting_data_delftstack[1]={"county":"El Paso","registered_voters":461149}
# output resulting voting_data_delftstack list
print(f"\nAfter 1., voting_data_delftstack list output is ...", (voting_data_delftstack), "\n")

# Remove "Arapahoe" and its registered voters from voting_data_delftstack
#   next five print code lines in this block modified from lstdict code on website...
#   https://www.delftstack.com/howto/python/python-search-list-of-dictionaries/
#   code line below returns dictionary item in voting_data_delftstack list that has "Arapahoe" as value for "county" key, None if not found
print(next((Look for Look in voting_data_delftstack if Look["county"] == "Arapahoe"), None))
#   code line below returns dictionary item in voting_data_delftstack list that has "not listed" as value for "county" key, None if not found
print(next((Look for Look in voting_data_delftstack if Look["county"] == "not listed"), None))
#   next code line returns index of dictionary item of voting_data_delftstack list that has "Arapahoe" as value for "county" key, None if not found
print(next((i for i, x in enumerate(voting_data_delftstack) if x["county"] == "Arapahoe"), None))
#   next code line returns index of dictionary item of voting_data_delftstack list that has "not in here" as value for "county" key, None if not found
print(next((i for i, x in enumerate(voting_data_delftstack) if x["county"] == "not in here"), None))
#
# print(next((i for i, x in enumerate(voting_data_delftstack) if x["county"] == "not found"), None))
#
# Module 3.2.7 (2) Remove "Arapahoe" and its registered voters from voting_data_delftstack.
#  2a) use .pop(index_value) method
ind_to_remove = next((i for i, x in enumerate(voting_data_delftstack) if x["county"] == "Arapahoe"), None)
if type(ind_to_remove) == None:
  print("No entry for Arapahoe county found")
else:
  #county_popped = voting_data_delftstack.pop(next((i for i, x in enumerate(voting_data_delftstack) if x["county"] == "Arapahoe"), None))
  county_popped = voting_data_delftstack.pop(next(i for i, x in enumerate(voting_data_delftstack) if x["county"] == "Arapahoe"))
voting_data_delftstack
#
# put the removed dictionary item back into the same position in the voting_data_delftstack list, then
#  2b) remove with .remove(list_item_to_remove) method
ind_was_removed = ind_to_remove
voting_data_delftstack.insert(ind_was_removed, county_popped)
# voting_data_delftstack.remove(next((Look for Look in voting_data_delftstack if Look["county"] == "no such county"), int(" ")))
voting_data_delftstack.remove(next((Look for Look in voting_data_delftstack if Look["county"] == "Arapahoe"), None))
#
# next line of code removes dictionary item of voting_data_delftstack list where "county" key has value "not found"...
# ...resulting in ValueError otherwise
# voting_data_delftstack.pop(next((i for i, x in enumerate(voting_data_delftstack) if x["county"] == "not found"), None))
# next line of code removes dictionary item of voting_data_delftstack list where "county" key has value "Arapahoe"...
# ...resulting in ValueError otherwise
##county_popped = voting_data_delftstack.pop(next((i for i, x in enumerate(voting_data_delftstack) if x["county"] == "Arapahoe"), None))
voting_data_delftstack

# Module 3.2.7 (3) Make "Denver" and its registered voters the third item in voting_data_delftstack,
# but keep "Jefferson" and its registered voters as the second item.
voting_data_delftstack.insert(2,{"county":"Denver","registered_voters":463353})
voting_data_delftstack

# Module 3.2.7 (4) Add "Arapahoe" and its registered voters to voting_data_delftstack.
voting_data_delftstack.append({"county":"Arapahoe","registered_voters":422829})

# output resulting voting_data_delftstack list
voting_data_delftstack
#
# from Module 3.2.9 ...
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
#
# later in Module 3.2.9 ...
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
#
# and later again in Module 3.2.9 ...
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
#
# Module 3.2.10 ...
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
print(f"\ncounties_dict output:\n{counties_dict}")
#
print('\noutput from:\tfor county in counties_dict:\
            \n\t\t\tprint(f"{type(county)} {county}")')
for county in counties_dict:
    print(f"{type(county)} {county}")
##
print('\noutput from:\tfor county in counties_dict.keys():\
            \n\t\t\tprint(f"{type(county)} {county}")')
for county in counties_dict.keys():
    print(f"{type(county)} {county}")
##
print('\noutput from:\tfor county in counties_dict.values():\
            \n\t\t\tprint(f"{type(county)} {county}")')
for county in counties_dict.values():
    print(f"{type(county)} {county}")
##
print('\noutput from:\tfor county in counties_dict:\
            \n\t\t\tprint(f"{type(county)} {county}\
            \t{type(counties_dict[county])} {counties_dict[county]}")')
for county in counties_dict:
    print(f"{type(county)} {county}\
      \t{type(counties_dict[county])} {counties_dict[county]}")
##
print('\noutput from:\tfor county in counties_dict:\
            \n\t\t\tprint(f"{type(county)} {county}\
            \t{type(counties_dict.get(county))} {counties_dict.get(county)}")')
for county in counties_dict:
    print(f"{type(county)} {county}\
      \t{type(counties_dict.get(county))} {counties_dict.get(county)}")
##
# skill drill :
print('\noutput from:\tfor ky,vl in counties_dict.items():\
            \n\t\t\tprint(f"{ky} county has {vl} registered voters.")')
for ky,vl in counties_dict.items():
    print(f"{ky} county has {vl} registered voters.")
##
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
print("\r")
for county_dict in voting_data:
    print(county_dict)
##
# Offset the next output from previous line...
print("\r")
##
# Multiline F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)
# Offset the next output from previous line...
print("\r")
##
# Format Floating-Point Decimals
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)
# Offset the next output from previous line...
print("\r")
#
# Module 3.2.11 skill drill one
# create the dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# Print each county and registered voter from the dictionary as pictured.
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")
# ^^^^^^ no repeatable difference noticed b/w runtime of code above vs below ...
for county, voters in counties_dict.items():
    print(f'{county} county has {voters:,} registered voters.')
#
# Offset the next output from previous line...
print("\r")
#
# Module 3.2.11 skill drill two
# create the list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
# Print each county and registered voter from the dictionary as pictured.
for current_dict in voting_data:
    print(f'{current_dict["county"]} county has {current_dict["registered_voters"]:,} registered voters.')
## ^^^^^ seems maybe 0.1 seconds faster ^^^^^^ than for loop code below ...
for current_dict in voting_data:
    print(f"{current_dict['county']} county has {current_dict['registered_voters']:,} registered voters.")
#
## Offset the next output from previous line...
#print("\r")
