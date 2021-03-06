# LootRoller
Creating a loot roller for D&amp;D, GURPS, and others.

This program will allow a user to create entities containing items, and to drop those items according to user-defined 
percentages.

## Changelog

######Pre-alpha

v0.0.10
- Add 'Items' submenu
  - Add 'Create' option
  - Add 'List' option
    - This option supports listing items in the master table as well as current unsaved changes.
  - Add 'Back' option
- Create 'lootroller.bat' file to easily execute the file for Windows users.

v0.0.09
- Begin overhaul of interface
  - Going to ditch state file in favor of a continuous loop
    - (Quietly questioning why I didn't opt for this in the first place)
  - Will be run with Items, NPC, Drop, Help, and Exit
    - Items will enter item related menu, NPC will enter NPC, Drop will drop etc
  - Will have a master database of all items and all NPCs and all NPC tables
    - This will allow for items to be created once and reused in other tables
    - Will also allow for easier editing of items across tables
  - NPCs will be able to have multiple tables, and a current, 'default' table
    - This will allow for NPCs to be reused later in the game. For instance, a reoccuring boss

v0.0.08
- Removed testing files, renamed cfgtest to chand
- Updated dictionary saving function (for real this time)
- Added 'show' option to main argument
- Added 'edit' option to main argument
  - Added 'create' and 'show' to 'edit' argument
- Corrected some spelling mistakes

v0.0.07
- Program is now run with lootroller.py
- Program is run with arguments [list, select, drop]
- Implemented basic statefile settings

v0.0.06
- Table saving function now has the ability to check if an item is already present in the file before saving, eliminating duplicates
- Added support for flavor text in item creation
- Added handling for flavor text in the table reader

v0.0.05
- Realized csv reader wasn't working as intended, changed file organization to better suite the way the reader reads
- Changed .csv extension to .loot, since its not really a csv anymore
- Made file for handling items, added item creation method to it
- Learned how to compile the program, eliminating the need to prefix with "python3 "

v0.0.04
- Added a csv writer to write to a file based on user input
- Picked colors for output text, will be implemented soon

v0.0.03
- Addressed the problem of storage and decided to use csv files. Since the program does not run constantly in memory, will need to create a state file to read from
- Added a csv reader function to pull text from the file into the program

v0.0.02
- Decided to use dictionaries to store items and their attributes
- Tested dropping items from a dictionary

v0.0.01
- Created initial random drop script, the core feature
