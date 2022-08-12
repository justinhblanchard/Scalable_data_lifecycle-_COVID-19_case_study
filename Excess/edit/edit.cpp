#include "edit.h"

void Data::read(){	
	string header = "";
	string temp = "";
	string file;
	int comma = 0;
	int num = 1;
	cout << "Input filename: ";
	cin >> file;
	ifstream fin;
	fin.open(file);
	getline(fin, header);
	for(int i = 0; i < (int) header.size(); i++){
		if(header[i] == ','){
			type.push_back(temp);
			temp = "";		
			comma++;
		}	
		else temp += header.substr(i, 1);	
	}
	type.push_back(temp);
	temp = "";
	cols = comma + 1;
	vector<vector <string> > vec(cols);
	for(int i = 0; i < (int) type.size(); i++) vec[i].push_back(type[i]);
	comma = 0;
	rows = 1;
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

void Data::readmax(){
	vector <vector <string> > vec(7);
	string cases = "";
	string deaths = "";
	string tests = "";
	string vac = "";
	string people = "";
	string fully = "";
	string boosters = "";
	string test = data[0][0];
	for(int i = 0; i < (int) data[0].size(); i++){
		if(test != data[0][i]){
			test = data[0][i];
			vec[0].push_back(cases);
			vec[1].push_back(deaths);
			vec[2].push_back(tests);
			vec[3].push_back(vac);
			vec[4].push_back(people);
			vec[5].push_back(fully);
			vec[6].push_back(boosters);
			cases = "";
			deaths = "";
			tests = "";
			vac = "";
			people = "";
			fully = "";
			boosters = "";
		}
		else{
			if(data[1][i] != "") cases = data[1][i];
			if(data[2][i] != "") deaths = data[2][i];
			if(data[3][i] != "") tests = data[3][i];
			if(data[4][i] != "") vac = data[4][i];
			if(data[5][i] != "") people = data[5][i];
			if(data[6][i] != "") fully = data[6][i];
			if(data[7][i] != "") boosters = data[7][i];
		}
	}
	data.clear();
	data = vec;
}

void Data::row(){
	int num;
	cout << "Insert row: ";
	cin >> num;
	for(int i = 0; i < (int) data.size(); i++) cout << data[i][num] << " ";
	cout << endl;
}

void Data::col(){
	int num;
	cout << "Insert column: ";
	cin >> num;
	for(int i = 0; i < (int) data[num].size(); i++) cout << data[num][i] << endl;
}

void Data::swaprow(){
	string temp;
	int num1;
	int num2;
	cout << "Insert row 1: ";
	cin >> num1;
	cout << "Insert row 2: ";
	cin >> num2;
	for(int i = 0; i < rows; i++){
		temp = data[num1][i];
		data[num1][i] = data[num2][i];
		data[num2][i] = temp;
	}
}

void Data::swapcol(){
	int num1;
	int num2;
	cout << "Insert colummn 1: ";
	cin >> num1;
	cout << "Insert colummn 2: ";
	cin >> num2;
	vector <string> temp;
	temp = data[num1];
	data[num1] = data[num2];
	data[num2] = temp;
}

void Data::combine(){
	string header = "";
	string temp = "";
	string file;
	int comma = 0;
	int count = 1;
	int newcols;
	cout << "Input filename: ";
	cin >> file;
	ifstream fin;
	fin.open(file);
	getline(fin, header);
	for(int i = 0; i < (int) header.size(); i++){
		if(header[i] == ','){
			type.push_back(temp);
			temp = "";		
			comma++;
		}	
		else temp += header.substr(i, 1);	
	}
	type.push_back(temp);
	temp = "";
	newcols = comma + 1;
	vector<vector <string> > vec(newcols + cols);
	for(int i = 0; i < (int) data.size(); i++) vec[i] = data[i];
	for(int i = (int) data.size(); i < (int) type.size() + (int) data.size(); i++) vec[i].push_back(type[i]);
	comma = 0;
	while(getline(fin, header)){
		for(int i = 0; i < (int) header.size(); i++){
			if(header[i] == ','){
				vec[comma + data.size()].push_back(temp);
				temp = "";		
				comma++;
			}	
			else temp += header.substr(i, 1);	
		}
		vec[comma + data.size()].push_back(temp);
		temp = "";	
		comma = 0;
		count++;
	}
	if(count > rows){
		for(int i = rows; i < count; i++){
			for(int j = 0; j < cols; j++) vec[j].push_back(temp);
		}
		rows = count;
	}
	else{
		for(int i = count; i < rows; i++){
			for(int j = cols; j < cols + newcols; j++) vec[j].push_back(temp);
		}
	}
	cols += newcols;
	data = vec;
	fin.close();
}

void Data::write(){
	ofstream fout("data.csv");
	for(int i = 0; i < (int) data[0].size(); i++){
		for(int j = 0; j < (int) data.size() - 1; j++) fout << data[j][i] << ",";
		fout << data[data.size() - 1][i] << endl;
	}
}

void Data::print(){
	for(int i = 0; i < rows; i++){
		for(int j = 0; j < cols; j++) cout << data[j][i] << " ";
		cout << endl;
	}
}

int main(){
	Data d;
	string usr;
	cout << "List of commands:" << endl;
	cout << "read - Reads in a file" << endl;
	cout << "row - Outputs a row" << endl;
	cout << "col - Outputs a col" << endl;
	cout << "swaprow - Swaps two rows" << endl;
	cout << "swapcol - Swaps two cols" << endl;
	cout << "combine - Adds a second file to the file in memory" << endl;
	cout << "write - Writes the file on memory" << endl;
	cout << "print - Prints the file on memory" << endl;
	cout << "quit - Exits the program" << endl;
	cout << "Command: ";
	d.read();
	d.readmax();
	d.write();
	/*while(cin >> usr){
		if(usr == "read") d.read();
		else if(usr == "row") d.row();
		else if(usr == "col") d.col();
		else if(usr == "swaprow") d.swaprow();
		else if(usr == "swapcol") d.swapcol();
		else if(usr == "combine") d.combine();
		else if(usr == "write") d.write();
		else if(usr == "print") d.print();
		else if(usr == "quit") return 1;
		else cout << "Invalid input" << endl << "Command: ";
	}*/
}