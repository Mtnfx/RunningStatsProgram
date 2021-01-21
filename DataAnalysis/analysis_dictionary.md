# Analysis Dictionary
This file will hold all of the ambiguous statistics terms I use throughout my spreadsheets and reports. Note that some of the terms are, to the best of my knowledge, made up by me.

### Quadratic/Cubic Deviation (n)
This term is how I describe the difference between the value of the quadratic/cubic curve of best fit equation and the expected value at the point *n* in brackets. It is an absolute value, such that I can fit an exponential function to the values to get a relationship and ensure my data gets closer to successful at roughly the speed I think it should.

### Factor of Superior Accuracy (Q over C)
This is a value that I display in Excel to 2 decimal points. This represents the number of times more efficient using a quadratic curve of best fit is rather than using a cubic curve. A value above 1 denotes that a quadratic curve is more efficent, a value of exactly 1 denotes both are equally effective and a value below 1 denotes that a cubic curve is more accurate.

### Generalized Algorithm [Prediction]
The generalized algorithm is a simplified model of the curve of best fit. The average of all times in a calendar year is taken and compressed into a single data point. The data points from every year are put into one model and a curve of best fit is attached to it. Since in my general model, the quadratic curve visibly undershoots an accurate time slightly and the cubic curve appears to overshoot an accurate time slightly, the average of the two curve of best fit values is taken to get an improved target value to check the more specific curves of best fit. 
