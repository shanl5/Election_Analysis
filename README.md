# Election_Analysis
Analysis of election data from three sources

## Election Audit Project Overview
A Colorado Board of Elections employee has tasked the project with completing an audit of a recent local congressional election; an audit comprised of two components as desribed below as parts [A] and [B].

[A]  Determine and provide to the election commision the following three items for counties involved in the election<sup>a</sup>:
	
  1. A full accounting of total votes cast in the election.
	
  2. The voter turnout for each county.
	
  3. The percentage of votes from each county out of the total count.
	
  4. The county with the highest turnout.

[B] Report the following five items for candidate results:
	
  5. A complete list of candidates receiving votes.
	
  6. The total number of votes received by each candidate.
	
  7. The percentage of total votes won by each candidate.
	
  8. The winner of the election based on popular vote.

<sup>a</sup> From Challenge Background

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.9 & 3.10.5, Visual Studio Code, 1.68.1
- Coding template framework: PyPoll_Challenge_starter_code.py

## Election-Audit Results

For Part [A]<sup>image i, image ii (below)</sup> , results show:
- A total of 369,711 votes were cast in the election.
- Votes were reported for three counties:
  - County 1 : Jefferson
  - County 2 : Denver
  - County 3 : Arapahoe
- These county results are summarized below:
  - Jefferson (county 1) had turnout of 10.5% of the vote, numbering 38,855 total votes.
  - Denver (county 2) had turnout of 82.8% of the votes, numbering 306,055 votes counted.
  - Arapahoe (county 3) had turnout of 6.7% of overall votes, or a total of 24,801 votes.
- The highest voter turnout was for: Denver county.

image i
-- The output to a terminal screen:

<img src="/Resources/analysis/Screenshot_2022-06-22_election_results_print-to-terminal.png" width="40%">

image ii
-- The results printed to a text file:
<img src="/Resources/analysis/Screenshot_2022-06-22_election_results_write-to-file.png" width="40%">

For Part [B]<sup>image i, image ii (above)</sup> the inspection and analysis of the data set reveals that:
- Three candidates received votes:
  - Candidate 1 : Charles Casper Stockham
  - Candidate 2 : Diana DeGette
  - Candidate 3 : Raymon Anthony Doane
- The candidate results are as below:
  - Candidate 1 received 23.0% of the vote, which is a number of 85,213 votes.
  - Candidate 2 received 73.8% of the vote, or a number equal to 272,892 votes.
  - Candidate 3 received 3.1% of the vote, or a total of 11,606 votes.
- The winner of the election was:
  - Candidate 2 -- Diana DeGette -- receiving a vote count of a number of 272,892 of the total 369,711 cast in the election, or 73.8% popular vote.

## Election-Audit Summary

Before any analysis can be performed, an understanding of the underlying data is essential, and in this case this understanding is eased by the uniform presentation of the election results data set. Accumulated from three voting methods sources -- mail-in ballots, punch cards, and direct-recording electronic (DRE) counting machines -- yet all sent to a central office, each line of the election results data set file holds information for a ballot ID, county, and candidate name receiving the vote. This uniformity (consistency) allows for an *accumulator* variable ("`total_votes`" in the code) to be used to tally project item (1).

For project items (5)<sup>iii</sup>, a Python "*list*" structure ("`candidate_options`" in the code) is "built" during the line-by-line reading of the election results file, holding after the file is read the unique candidate names. Similarly, another Python data structure, a "*dictionary*" ("`candidate_votes`" in the code) is built during the election results file open-and-read (refer to "`with`" and subsequent "`for`" statements in the code), so that at the end of the file reading, the dictionary holds keys matching the names in the `candidate_options` list and values equal to the votes received by that candidate; this completes the tally of project item (6). Project items (3) and (7), respectively county and candidate vote percentage, are calculated items found by formula combining entries from the "`county_votes-dict`" {"`candidate_votes`"} dictionaries and the "`total_votes`" accumulator; i.e. respective "county turnout"{"candidate"}_`vote_percentage` = "county"{"candidate"}_`votes` / `total_votes` * 100. 

Finally, project item (8), the winner of the election, is determined by checking through the "`candidate_votes`" dictionary which candidate (utilizing "`candidate_name`" in the code) has the highest (compared to a default "`winning_count`" votes of zero) and highest percentage (compared to a default "`winning_percentage`" of zero) for candidate_`votes` and candidate_`vote_percentaage`.

![image iii](https://github.com/shanl5/Election_Analysis/blob/main/Resources/analysis/Screenshot_2022-06-22_PyPoll_Challenge_pythonscript-snip.png)

**Notes**:
- Aside from the issues encountered in this module with learning the intricacies of the new programming language syntax and data structures -- these (yet  to be) overcome by practice! practice! practice! (and still ongoing practice) -- another more concrete problem-solution pair dealt with software setup. In      particular, the recommendation (TA office hours) was to check the box relating to Python>Terminal window in VS Code settings for "Execute in File Directory" so that opening the election_results.csv text file no longer resulted in a "FileNotFoundError" (something relating to relative versus absolute path?)

- Also, as per Module 3 instructions, "csv" and "os" *dependencies* are required to be imported at the beginning of the PyPoll.py file, which respectively bring in to the program CSV text file read capability; and interaction capability with the computer operating system, enabling access to features such as specifying file "`path`" and opening and writing to files. 

- While it is possible to perform this analysis with the spreadsheet and programming tools encountered recently in the last couple modules, the power of the Python language to "access, process, manipulate, and store data"<sup>{The Power of Python Video from Module 3.0.1}</sup> enables the production of repeatable code sequences to analyze speedily very large data sets. This segues into the proposed recommendation ...

### **Summary Recommendation**

Although the eight-pronged audit here may be accomplished using with Excel and VBA, already-learned application software from ealier module work, the challenge here is to *automate* the audit with Python by reading in a CSV text file of the election results and outputting the analysis to another text file in addition to a standard output command screen. If done successfully, this automation may be used to analyze results from other districts and elections.

And with understanding that this may be the ultimate goal, the project can recommend the following ways the script may be modified to be used for other elections:
- Add a prompt for a *location* (e.g. a computer directory, or other name of file) of a similarly formatted CSV text file that will be read in and reviewed for tallying results, rather than the fixed location of a folder called "Resources" now that holds a file that must be named "election_results.csv"
- The "County" column variables and printing information may be changed to reflect other types of elections, e.g. Congressional District elections rather than coded as now to always report "County" data.
- Allow the code to determine names and order of columns from the data file itself; so, e.g., continuing with the Congressional District election example, the second column may be named "District" rather than "County," and a "Ballot ID" may be the third rather than first column, with Candidate name being perhaps in the initial (index 0) column.
