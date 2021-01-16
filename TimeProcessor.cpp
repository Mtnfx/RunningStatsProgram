#include <iostream>
#include <string>
#include <vector>
using namespace std;

//This class holds all time information. Only exists in case I need to write
//time manipulating functions.
class chron{
	public:
	int min;
	double sec;
	chron(int m, double s){
		min = m;
		sec = s;
	}
};

//------------------------------------------------------------------------------
//This class holds all information of a single runner in a race.
class runner{
	chron baseTime;
	chron actualTime;
	string first;
	string last;
	runner(chron b, string f, string l){
		first = f;
		last = l;
		baseTime = b;
		actualTime = NULL;
	}
};

//------------------------------------------------------------------------------
//This class will hold all the members of a single team if I decide to write it.
class team{
	
};

//------------------------------------------------------------------------------
//Use statistics magic/bullshit to generate a practical time.
chron generateTime(chron base){
	
}

//------------------------------------------------------------------------------
int main(){
	chron newTime = chron(4,12);
	cout << newTime.min << ":" << newTime.sec;
	return 0;
}