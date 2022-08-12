#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

class Data{
	public:
		vector <string> categories;
		vector <string> types;
		vector <string> descriptions;
		vector <vector <string> > data;
        int rows;
        int cols;
        void readmetadata(string file);
		void read(string file);
		void write();
};

class Stats{
    public:
        vector <string> x;
        vector <string> y;
        vector <string> headers;
        vector <vector <double> > heatmap;
        int n;
        double sumx;
        double sumy;
        double meanx;
        double meany;
        double stddevx;
        double stddevy;
        double covariance;
        double correlation;
        double m;
        double b;
        void regression(vector <string> vec1, vector <string> vec2);
        void heat(Data d);
        void write();
};