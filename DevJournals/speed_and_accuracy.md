# Processing Speed and Accuracy

The two most important factors in making this project work well are the speed at which the simulation can run every oiperation and compile all the data and the accuracy of the data processed. Since generally more calculations done on the data will yield higher accuracy but also take the program longer to execute, a certain balance of speed and accuracy must be maintained.

### Speed
With small fields, I'm not too worried about speed. Usually I have all the time I need to compile the data and run it through the program. However, when it comes to larger fields in the hundreds, even a few unneccessary operations can cause a whole lot of time to be wasted. To keep my computer from overheating and to reduce the amount of time I have to sit at my computer waiting for it to compile, the following must be done:
  * Minimize the number of variables in use
  * Minimize the number of calculations done and cut out any statistically insignificant calculations
  * Minimize the number of loops, especially nested ones

### Accuracy
Accuracy is a bit more complicated. Theoretically, the more times I run the program to simulate, the more likely I am to get accurate results. However, the more times I run the program, the closer on average the simulations will get to the theoretical value. Given that the whole point of my program is to avoid outputting the ideal value, I usually only run 1 simulation if time and placing matter. However, if I want to generate probabilities, for the exact same reason, I will run the program 10000 times and list the percent chance that someone finished in the top *n* places as *q/10000 multiplied by 100%* where *q* is the number of times the given runner finished in the top *n* places of the race.

In summary:
  * If time and place matter, simulate once to get a degree of variability and save speed
  * If overall probability of finishing at least *nth* matters, simulate lots of times and take the percent of simulations where the runner finished in the top *n* places

Overall, I care about accuracy a lot more than I do speed. However, it is very good to cut down any unneccessary runtime if possible as it makes my job easier. For time and placing simulations, ideally my accuracy will be about 90-95% across the board. For percent simulations, it's a bit harder to determine what defines accuracy so I will ponder that for a bit longer and get back with a better idea.
