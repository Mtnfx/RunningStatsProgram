# Generating Estimates
Before I even deal with generating practical times, I first need to worry about generating accurate theoretical times. I will do so based on the data I have from previous races and correlate this with as many variables as possible to increase the accuracy of my estimates. Here are my current strategies for dealing with getting an accurate generation of each factor:

### Age vs Time
Age is probably the most important factor to get right since its the only factor I am able to get exact values for at the moment (at least for more well known runners like Olympians). Fortunately for me, it only took me 10 years of working in Microsoft Excel to figure out that Excel can do date subtraction. This means that I can calculate the age of a runner if I know their birthday (again, this really only works for Olympians since I can get this data online) and the date at which the race was run. I will do so using the formula *(a - b)/365.25* where *a* is the date on which the race was run and *b* is the birthday of the runner in question. Taking the age of the runner as the independent variable and the time they ran at that age as the dependent, I can create a data point. Given enough data points for a long enough period of time, I can theoretically create a relatively accurate model of how the runner will perform in the future.

The easiest way to fit a good selection of age vs time data points into a statistical model given my limited knowledge of statistics is to use a quadratic curve of best fit. A quadratic model is intuitively the best to start with since when ignoring all other factors and purely isolating age and time, you'd expect a child to get faster as they reach young adulthood and then begin to slow down as they get to be middle aged.

Of course, there are a few problems with this correlation. For one, most types of running races span across only one season. for example, track season is usually only in late spring to early summer. Given this, there are large holes in data which most likely recuce the accuracy of the model by quite a bit.