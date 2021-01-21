# Connection of Different Languages
As of January 21st 2021, I have decided to use R for processing databases. Due to this, I will outline a very broad outline of how I plan to switch between multiple languages to make my code run relatively smoothly.

As of January 21st 2021, the plan is as follows:

##### Start
###### Data Type: Raw Data
1. Process raw data in a "simple" language (I'm using Python unless I find out I can't do some of the more complex math stuff in Python). This will generate practical times for each runner in the data set.
###### Data Type: Analyzed Data
2. Transfer data to database language (R) to clean.
3. Sort data ascending based on the generated practical times
###### Data Type: Clean Data
4. Merge multiple sets of clean data from different divisions together to create a new set of data (This step is only necessary if running competitions span multiple rounds)
###### Data Type: Raw Data
5. Start at the top of the algorithm and repeat for subsequent rounds of competition
##### End

To allow me to execute all of this in one step, I use Batch to string together Python and R scripts so that they run back to back.

I do hope that these journals are clear enough to understand. The main reason I write these is so that if anyone comes across this project, especially younger or new programmers, they undestand how it works.
