# Data Skews

There are several varying factors that lead to my analysis most likely being slightly off. In this section, I will outline the most common causes of error that I anticipate will mess up my analysis.

#### Weather Conditions
Various conditions like wind speed, temperature, and precipitation will cause my data to be slightly off. Hopefully, I may be able to fit a linear or quadratic line/curve of best fit to a few of these factors to reduce interference. This factor fortunately should not impact indoor events.

#### Injury and/or Abnormally Poor Performance
Injuries will clearly slow down a runner if they even choose to run. A simple constant multiplier or a linear scale based on injury severity to account for injury may be sufficient. Usually abnormally poor performance or midrace injury is almost impossible to predict or account for so I do not predict a part of my model will ever be able to account for outlying poor performance.

#### Age
Age impacts every runners' performance slightly differently. I anticipate that the best I can manage until I get a better education in statistics is a simple quadratic or possibly cubic curve analysis to generalize the impact of age of running times.

#### Terrain
Terrain will only ever be a crucial factor in cross country races or road races. Track events will ignore this. Terrain is especially hard to account for if:
  * The terrain of the course is unknown
  * There is no previous race data for the course

Needless to say, if the rough difficulty of the course terrain is known, I can estimate that a similar amount of time will be lost on this course compared to courses I list as having a similar difficulty. If there is previous race data on this course, I can look at how runners who have already ran this course ran other courses and extrapolate the data to get fairly decent estimates of how much the terrain  of a course will slow down runners who are new to the course.

If there are any factors that I have failed to mention that you deem important, feel free to tell me as I am always looking for new suggestions to make my work even better.
