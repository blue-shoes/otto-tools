!!NOTICE!! 

This repository is archived as of 1/2/2023. Functionality and open issues hav been moved to the Ottoneu Toolbox repository for a fuller user experience (https://github.com/blue-shoes/ottoneu-toolbox). 

# Otto-Tools

## Project Description
The Otto-Tools project is a package of python-based UI tools for playing Ottoneu Fantasy Baseball. As a player of Ottoneu Fantasy Baseball for seven years, I've found 
myself often creating side tools to accomplish various tasks to give me an edge in the game, almost always using Excel spreadsheets. Once these became too bulky
to be useful, I began creating robust tools in Python with a GUI to facilitate these tasks. I am now sharing these tools with the public at large.

## Installation Instructions
Users may clone the repo with 
```git clone https://github.com/blue-shoes/otto-tools```

Alternatively, period tool releases will contain executable files that can be downloaded and run by the user. Note that currently these executables are unsigned and 
will likely trigger a Windows Defender warning stating so the first time they are executed.

## Current Tools

### Ottoneu Draft Tool
Current Version: v0.8.1
The Ottoneu Draft Tool allows users to load their own sets of player values for Fangraphs Points or SABR Points leagues and use those in a live draft to monitor 
available players in near-real-time. The ability to search for players within the Ottoneu universe is given at the top, including partial matching and handling of
diacritics. Tables of the top available overall players and by Ottoneu position are provided below. The tables are updated in-draft at a rate of once a minute when
the user begins draft monitoring using the available start button, removing players and update the league inflation rate.

![image](https://user-images.githubusercontent.com/61890211/160003776-1a0b6d03-1fd7-40c4-a19c-3ebf1eca3c2e.png)

Uploading values requires a csv file named values.csv or ottoneu_values.csv with at minimum the following columns:
- Id (either Fangraphs Id or Ottoneu Id) ! This must be the first column !
- Ottoneu Id (if the Id column is Fangraphs Id)
- Value or price
- Name
- Position(s) or Pos
- FGPts, SABRPts, or Points
- FGPtspG, SABRPtspG, or P/G
- FGPtspIP, SABRPtspIP, or P/IP

The format of the file produced by https://ottovalues.shinyapps.io/FGPts and https://ottovalues.shinyapps.io/SABR_Points/ is designed to conform to these requirements. 
In addition, if the user wants custom positional rankings (rather than the point rate rankings automatically provided by the tool), they may include files of the same
format titled [pos]_values.csv where [pos] is the Ottoneu position title.

## Work in Progress
The current verison v0.8.1 is considered a Minimum Viable Product (MVP), with room for expansion. Potential feature expansions include:
- Addition of 4x4 and 5x5 formats
- Ability to toggle view to show or hide drafted players
- Current Ottoneu Universe salary information for each player
- Ability to identify targets in the tables
- Ability to view stats/projections for individual players on-demand
