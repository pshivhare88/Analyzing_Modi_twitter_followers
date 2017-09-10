# Analyzing a sample of Narendra Modi's Twitter Followers
## Project Description:
---
The project involves extracting twitter information of Narendra Modi's followers, translating the location text to english, cleaning the location field, and analyzing the geography of Modi's followers.

## Project Objective:
---
To understand how the popularity of Narendra Modi on twitter varies by geography

## Code Description:
---
- **data_extraction.py:** This python script accesses twitter api and extracts twitter information of the followeres of a twitter account entered by the user. For this project, we will extract twitter information of Narendra Modi's followers. The extracted information is stored in a sqlite database.

- **translate.py:** This python script accesses microsofttranslator api and transaltes the location string in the sqlite database created by data_extraction.py script

- **cleanse.py:** This python script cleans the location string to standard 2 character ISO country codes.

## Project Challenges:
- **Data Extraction from Twitter:** Twitter rate limiting allows to extract information of 3000 followers every 15 mins. At this rate it would take running the extraction code for 4 months without disruption to extract information of all 31 Million followers of Mr. Modi. Due to time restrictions I extracted only a sample of 2.6 M users. Out of 2.6 M, 1.6 Million users had missing location. Finally, the heatmap visualization was created on the basis of a sample of 0.8 Million.

## Disclaimer:
---
This project was done to demonstrate python scripts extract twitter api. This analysis is not accurate as it is only based out of a sample. The results of this analysis are not to be qouted in any situation to drive decision making. 

