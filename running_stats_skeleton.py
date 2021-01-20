class Runner:
    def __init__ (self, first, last, base):
        self.first = first
        self.last = last
        #Note that all times will be expressed in seconds
        self.base = base
        #Just to be sure I don't confuse this with a final value, it is negative
        #which is of course nonsense
        self.prac_time = -1

def process_data():
    data = open("test_data_small.csv")
    race_list = []
    for line in data:
        #Remove endline character from each line
        line = line.strip()
        #Separate entries of character object into separate variables
        line = line.split(',')
        #Connect each data point to a variable
        first_name = line[0]
        last_name = line[1]
        base_time = line[2]
        #Compile data points into a runner object
        runner = Runner(first_name, last_name, base_time)
        #Add the runner's information to the list of runners
        race_list.append(runner)
    return race_list
 
#Test run just in case something fails      
start_list = process_data()
print(start_list)
#It returns 4 runner objects so it most likely succeeds. Thus, this preliminary
#skeleton is successful