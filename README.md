# LootRoller
Creating a loot roller for D&amp;D, GURPS, and others.

This program will allow a user to create entities containing items, and to drop those items according to user-defined 
percentages.

## Versions

######Pre-alpha

v0.0.05
- Realized csv reader wasn't working as intended, changed file organization to better suite the way the reader reads
- Changed .csv extention to .loot, since its not really a csv anymore
- Made file for handling items, added item creation method to it
- Learned how to compile the program, eliminating the need to prefex with "python3 "

v0.0.04
- Added a csv writer to write to a file based on user input
- Picked colors for output text, will be implimented soon

v0.0.03
- Addressed the problem of storage and decided to use csv files. Since the program does not run constantly in memory, will need to create a state file to read from
- Added a csv reader function to pull text from the file into the program

v0.0.02
- Decided to use dictionaries to store items and their attributes
- Tested dropping items from a dictionary

v0.0.01
- Created initial random drop script, the core feature
