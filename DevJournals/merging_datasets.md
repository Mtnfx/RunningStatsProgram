# Merging Datasets
In multiple round competitions, it is important to track who qualifies for the higher rounds. In order to derive the fields for upper rounds of running races, I have to be able to effectively merge multiple datasets together. Here is my current plan for doing that:
  * All datasets have their own csv file
  * There will be one central file that holds advanced information for each dataset such as the destination file of runners who qualify for the next round, the tier of the file, and the number of runners that can qualify from each file (assuming a set number qualify from each race)
  * If the top times regardless of heat qualify, the files get merged first and then the top however many times get moved to the next file.
  
  More specific information regarding all variables in the central file:
  ###### File
  This has the filename of the file the information is connected to
  
  ###### Destination File
  The file in which the appropriate number of runners get sent to after this file's race is simulated
  
  ###### Tier
  This is the round of races the file is associated with. The higher the tier, the later the round. This is used as a failsafe to ensure later rounds do not get simualted before all of their data is in the file.
  
  ###### Number Qualifying
  This is the maximum number of runners that can move intot eh next round. If there are less runners in the file than this number specifies can move on, all runners move on to the next round. A value of NA signifies that the races are over and tells the program to stop simulating.
  
