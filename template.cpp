#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main () {
  ifstream myfile;
  myfile.open ("../input");
  vector<string> guardLogs;
  if (myfile.is_open()) {
    string mystring;
    while(getline(myfile, mystring)) {
      guardLogs.push_back(mystring);
    }
  }
  myfile.close();
}