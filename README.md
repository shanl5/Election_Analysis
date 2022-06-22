# Election_Analysis
Analysis of election data from three sources

## Project Overview
A Colorado Board of Elections employee has tasked the project with completing an audit of a recent local congressional election. Specifically, to be determined and reported are the following five items:

1. A full tally of total votes cast in the election.
2. A complete list of candidates receiving votes.
3. The total number of votes received by each candidate.
4. The percentage of total votes won by each candidate.
5. The winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.9 & 3.10.5, Visual Studio Code, 1.68.1

## Summary
The inspection and analysis of the data set reveals that:
- A total of 369,711 votes were cast in the election.
- Three candidates received votes:
  - Candidate 1 : Charles Casper Stockham
  - Candidate 2 : Diana DeGette
  - Candidate 3 : Raymon Anthony Doane
- The candidate results are as below:
  - Candidate 1 received 23.0% of the vote, which is a number of 85,213 votes.
  - Candidate 2 received 73.8% of the vote, or a number equal to 272,892 votes.
  - Candidate 3 received 3.1% of the vote, or a total of 11,606 votes.
- The winner of the election was:
  - Candidate 1 -- Diana DeGette -- who received 73.8% popular vote, a number of 272,892 of the total 369,711 cast in the election.

## Challenge Overview
Although the five-pronged task at hand may be completed with Excel and VBA, already-learned application software presented in an earlier module, the challenge in this project is to *automate* this undertaking with Python by reading in a CSV text file of the election results and outputting the analysis to another text file in addition to a standard output screen. If done successfully, this automation may be used to analyze results from other districts and elections.

## Challenge Summary
Before any analysis can be performed, an understanding of the underlying data is essential, and in this case this understanding is eased by the uniform presentation of the election results data set. Accumulated from three voting methods sources -- mail-in ballots, punch cards, and direct-recording electronic (DRE) counting machines -- yet all sent to a central office, each line of the election results data set file holds information for a ballot ID, county, and candidate name receiving the vote. This uniformity (consistency) allows for an *accumulator* variable ("`total_votes`" in the code) to be used to tally project item (1).

For project item (2), a Python list structure ("`candidate_options`" in the code) is "built" during the line-by-line reading of the election results file, holding after the file is read the unique candidate names. Similarly, another Python data structure, a dictionary ("`candidate_votes`" in the code) is built during the election results file open-and-read (refer to "`with`" and subsequent "`for`" statements in the code), so that at the end of the file reading, the dictionary holds keys matching the names in the `candidate_options` list and values equal to the votes received by that candidate; this completes the tally of project item (3). Project item (4), a candidate vote percentage, is completed by utilizing a formula combining entries from the "`candidate_votes`" dictionary and the "`total_votes`" accumulator; essentially (in pseudo-code) candidate_`vote_percentage` = candidate_`votes` / `total_votes` * 100. 

Finally, project item (5), the winner of the election, is determined by checking through the "`candidate_votes`" dictionary which candidate (utilizing "`candidate_name`" in the code) has the highest (compared to a default "`winning_count`" votes of zero) and highest percentage (compared to a default "`winning_percentage`" of zero) for candidate_`votes` and candidate_`vote_percentaage`.

*Notes*:
- Aside from the difficulties encountered in this module with learning the intricacies of the new programming language syntax and data structures -- difficulties (yet  to be) overcome by practice! practice! practice! (and still ongoing practice) -- another more concrete problem-solution pair dealt with software setup. In      particular, the recommendation (TA office hours) was to check the box relating to Python>Terminal window in VS Code settings for "Execute in File Directory" so that opening the election_results.csv text file no longer resulted in a "FileNotFoundError" (something relating to relative versus absolute path?)

- Also, as per Module 3 instructions, "csv" and "os" dependencies are required to be imported at the beginning of the PyPoll.py file.

- While possible to perform this analysis with known historical languages and applications from our toolkit, learned and reinforced recently in the last couple modules, this module sets forth that exploring the strengths of another programming language introduces budding programming and analyst sensibilities to the power of the Python language to "access, process, manipulate, and store data"<sup>{The Power of Python Video from Module 3.}</sup> and may enable the production of repeatable code to analyze very large data sets.
