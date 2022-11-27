#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

const int REGION_EDGE_DISTANCE = 50;
const int DIMENSION = 2 * REGION_EDGE_DISTANCE + 1;

vector<string> split(string s, string delimiter) {
  vector<string> results;
  size_t pos = 0;
  string token;
  while ((pos = s.find(delimiter)) != string::npos) {
      token = s.substr(0, pos);
      results.push_back(token);
      s.erase(0, pos + delimiter.length());
  }
  results.push_back(s);
  return results;
}

void setCubeValues(int (&cubes)[DIMENSION][DIMENSION][DIMENSION], const vector<pair<int, int>> &ranges, int value) {
  for (int x = ranges[0].first; x <= ranges[0].second; x += 1) {
    for (int y = ranges[1].first; y <= ranges[1].second; y += 1) {
      for (int z = ranges[2].first; z <= ranges[2].second; z += 1) {
        cubes[x][y][z] = value;
      }
    }
  }
}

int main () {
  ifstream myfile;
  myfile.open ("../input");
  vector<string> lines;
  if (myfile.is_open()) {
    string lineString;
    while(getline(myfile, lineString)) {
      lines.push_back(lineString);
    }
  }
  myfile.close();

  int cubes[DIMENSION][DIMENSION][DIMENSION];
  for (int x = 0; x < DIMENSION; x += 1) {
    for (int y = 0; y < DIMENSION; y += 1) {
      for (int z = 0; z < DIMENSION; z += 1) {
        cubes[x][y][z] = 0;
      }
    }
  }

  for (string line : lines) {
    bool turnOn = line[1] == 'n';
    string rangeString = line.substr(turnOn ? 3 : 4);
    vector<pair<int, int>> ranges;
    for (string rangeStringItem : split(rangeString, ",")) {
      vector<string> rangeCoordinates = split(rangeStringItem.substr(2), "..");
      ranges.push_back(
        make_pair(
          max(stoi(rangeCoordinates[0]) + REGION_EDGE_DISTANCE, 0),
          min(stoi(rangeCoordinates[1]) + REGION_EDGE_DISTANCE, DIMENSION - 1)
        )
      );
    }
    
    setCubeValues(cubes, ranges, turnOn == true ? 1 : 0);
  }

  int nOnCubes = 0;
  for (int x = 0; x < DIMENSION; x += 1) {
    for (int y = 0; y < DIMENSION; y += 1) {
      for (int z = 0; z < DIMENSION; z += 1) {
        nOnCubes += cubes[x][y][z] ? 1 : 0;
      }
    }
  }
  cout << nOnCubes << endl;
}
