# RunningStatsProgram
This is just a recreational project.
If you happened to stumble across this, welcome!

This program seeks to be able to analyze the previous races of runners and somewhat accurately predict their finishing times in future races.

# Accuracy
I measure accuracy in races on a 50/50 weighted scale. Note that I am not very creative and this is the best system I have come up with so far.

The first 50% is placing accuracy. This is calculated by taking the number of places difference between what place my program predicted the runner would finish in and what place they actually did finish in and dividing by the size of the field. The average of this value for every runner in the field gives the final placement accuracy score.
I have relatively strong reasons to believe that this algorithm does not accurately reflect the actual accuracy of the simulation (given that my first prototype with questionable statistical estimation scored a 94% on the first and only trial of it). Thus, I have decided to add in the second half of the accuracy formula.

The second 50% is time accuracy. This is calculated using the percent error formula and subtracting that given value from 100% to get a percent accuracy. The mean of all these accuracy values over the whole field is the timing accuracy. This is new and not tested in my prototype version so I do not have a benchmark accuracy value.

# Recommended Readings
Most people can probably figure out how my code works based on documentation and syntax. However, I also do a good amount of planning in my Development Journals. I would personally recommend reading Base Assumptions as it gives a foundation as to what you automatically assume about my code.

# A Final Note
This project has been in the the works on paper for a while and in code for an almost equally long time. I've put this online to hopefully inspire anyone who's like me to delve a bit further into computing and statistics. The project you see here now will most likely continue to evolve as I get better at statistics and computer science (hopefully getting more accurate). That being said, I hope you enjoy looking through my project and seeing what kinds of ideas I have.

Regards,

Mountain Fox
