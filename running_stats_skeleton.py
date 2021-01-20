from typing import List

class Runner:
    def __init__ (self, first, last, base):
        self.first = first
        self.last = last
        #Note that all times will be expressed in seconds
        self.base = base
        #Just to be sure I don't confuse this with a final value, it is negative
        #which is of course nonsense
        self.prac_time = -1

def process_data(file: str) -> List[Runner]:
    """
    Return a list of runner objects using the data contained in file.
    
    Precondition: The file specified by variable file exists and is not empty.
    """
    data = open(file)
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

def generate_practical_time(race_list: List[Runner]) -> List[Runner]:
    """
    Return a modified version of race_list with added practical times.
    """
 
#Test last implemented feature of code  
start_list = process_data("test_data_small.csv")
print(start_list)
#Small set of test data is deemed to be successful
