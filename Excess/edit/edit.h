#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

class Data{
	public:
		vector <vector <string> > data;
		vector <string> type;
		int rows;
		int cols;
		void read();
		void readmax();
		void row();
		void col();
		void swaprow();
		void swapcol();
		void combine();
		void write();
		void print();
};