#include "stats.h"

void Data::readmetadata(string file){
    string temp = "";
    string usr;
	ifstream fin;
	fin.open(file);
	getline(fin, usr);
	for(int i = 0; i < (int) usr.size(); i++){
		if(usr[i] == ','){
			categories.push_back(temp);
			temp = "";		
		}	
		else temp += usr.substr(i, 1);	
	}
	categories.push_back(temp);
	temp = "";	
	getline(fin, usr);
	for(int i = 0; i < (int) usr.size(); i++){
		if(usr[i] == ','){
			types.push_back(temp);
			temp = "";		
		}	
		else temp += usr.substr(i, 1);	
	}
	types.push_back(temp);
	temp = "";	
	getline(fin, usr);
	for(int i = 0; i < (int) usr.size(); i++){
		if(usr[i] == ','){
			descriptions.push_back(temp);
			temp = "";		
		}	
		else temp += usr.substr(i, 1);	
	}
	descriptions.push_back(temp);
	fin.close();
}

void Data::read(string file){	
	string header = "";
	string temp = "";
	int comma = 0;
	int num = 1;
	cols = categories.size();
	rows = 0;
	ifstream fin;
	fin.open(file);
	vector<vector <string> > vec(cols);
	while(getline(fin, header)){
		for(int i = 0; i < (int) header.size(); i++){
			if(header[i] == ','){
				vec[comma].push_back(temp);
				temp = "";		
				comma++;
			}	
			else temp += header.substr(i, 1);	
		}
		vec[comma].push_back(temp);
		temp = "";	
		comma = 0;
		rows++;
	}
	data = vec;
	fin.close();
}

void Data::write(){
	ofstream fout("heatmap.csv");
	for(int i = 0; i < rows; i++){
		for(int j = 0; j < cols - 1; j++) fout << data[j][i] << ",";
		fout << data[cols - 1][i] << endl;
	}
}

void Stats::regression(vector <string> vec1, vector <string> vec2){
    x = vec1;
    y = vec2;
    n = x.size();
    sumx = 0;
    sumy = 0;
    for(int i = 0; i < n; i++){
        sumx += stod(x[i]);
        sumy += stod(y[i]);
    }
    meanx = sumx / n;
    meany = sumy / n;
    stddevx = 0;
    stddevy = 0;
    covariance = 0;
    for(int i = 0; i < n; i++){
        stddevx += pow(stod(x[i]) - meanx, 2);
        stddevy += pow(stod(y[i]) - meany, 2);
        covariance += (stod(x[i]) - meanx) * (stod(y[i]) - meany);
    }
    stddevx /= n;
    stddevy /= n;
    stddevx = pow(stddevx, 0.5);
    stddevy = pow(stddevy, 0.5);
    covariance /= n;
    correlation = covariance / (stddevx * stddevy);
    m = correlation * stddevy / stddevx;
    b = meany - (m * meanx);
}

void Stats::heat(Data d){
	vector <int> nums;
	for(int i = 0; i < d.cols; i++){
		if(d.types[i] == "double"){
			nums.push_back(i);
			headers.push_back(d.categories[i]);
		}
	}
	vector <vector <double> > vec(nums.size());
	for(int i = 0; i < (int) nums.size(); i++){
		for(int j = 0; j < (int) nums.size(); j++){
			regression(d.data[nums[i]], d.data[nums[j]]);
			vec[j].push_back(correlation);
		}
	}
	heatmap = vec;
}

void Stats::write(){
	ofstream fout("heatmap.csv");
	fout << ",";
	for(int i = 0; i < (int) headers.size() - 1; i++) fout << headers[i] << ",";
	fout << headers[headers.size() - 1] << endl;
	for(int i = 0; i < (int) heatmap.size(); i++){
		fout << headers[i] << ",";
		for(int j = 0; j < (int) heatmap.size() - 1; j++) fout << heatmap[j][i] << ",";
		fout << heatmap[heatmap.size() - 1][i] << endl;
	}
}

int main(int argc, char *argv[]){
    string temp = argv[1];
    temp = temp.substr(0, temp.size() - 3);
    temp += "mdt";
	Data d;
    d.readmetadata(temp);
	d.read(argv[1]);
    Stats s;
    s.heat(d);
	s.write();
}