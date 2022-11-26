#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int PADDING_SIZE = 100;

void addEmptyLine(vector<string> & trenchMap, int imageWidth) {
  for (int i = 0; i < PADDING_SIZE; i += 1) {
    string emptyLine(imageWidth + (2 * PADDING_SIZE), '.');
    trenchMap.push_back(emptyLine);
  }
}

void printTrench(vector<string> & trenchMap) {
  for (int i = 0; i < trenchMap.size(); i += 1) {
    for (int j = 0; j < trenchMap[0].size(); j += 1) {
      cout << trenchMap[i][j];
    }
    cout << endl;
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

  string imageEnhancer = lines[0];

  vector<string> trenchMap;
  int IMAGE_HEIGHT = lines.size() - 1;
  int IMAGE_WIDTH = lines[2].size();

  addEmptyLine(trenchMap, IMAGE_WIDTH);
  for (int i = 2; i < IMAGE_HEIGHT; i += 1) {
    string imageLine = "";
    for (int j = 0; j < PADDING_SIZE; j += 1) {
      imageLine.push_back('.');
    }
    for (int j = 0; j < IMAGE_WIDTH; j += 1) {
      imageLine.push_back(lines[i][j]);
    }
    for (int j = 0; j < PADDING_SIZE; j += 1) {
      imageLine.push_back('.');
    }
    trenchMap.push_back(imageLine);
  }
  addEmptyLine(trenchMap, IMAGE_WIDTH);
  
  for (int n = 0; n < 50; n += 1) {
    vector<string> newTrenchMap;
    for (int i = 0; i < trenchMap.size(); i += 1) {
      if (i < 1 || i > trenchMap.size() - 2) {
        string emptyLine(trenchMap[0].size(), n % 2 == 0 ? imageEnhancer[0] : '.');
        newTrenchMap.push_back(emptyLine);
        continue;
      }
      string newTrenchMapLine;
      for (int j = 0; j < trenchMap[0].size(); j += 1) {
        if(j < 1 || j > trenchMap[0].size() - 2) {
          newTrenchMapLine += n % 2 == 0 ? imageEnhancer[0] : '.';
        } else {
          string binIndex = "";
          binIndex += trenchMap[i - 1][j - 1];
          binIndex += trenchMap[i - 1][j];
          binIndex += trenchMap[i - 1][j + 1];
          binIndex += trenchMap[i][j - 1];
          binIndex += trenchMap[i][j];
          binIndex += trenchMap[i][j + 1];
          binIndex += trenchMap[i + 1][j - 1];
          binIndex += trenchMap[i + 1][j];
          binIndex += trenchMap[i + 1][j + 1];
          for (int k = 0; k < binIndex.size(); k += 1) {
            binIndex[k] = binIndex[k] == '.' ? '0' : '1';
          }
          int index = stoi(binIndex, 0, 2);
          newTrenchMapLine += imageEnhancer[index];
        }
      }
      newTrenchMap.push_back(newTrenchMapLine);
    }
    trenchMap = newTrenchMap;
  }

  int nLitPixels = 0;
  for (int i = 0; i < trenchMap.size(); i += 1) {
    for (int j = 0; j < trenchMap[0].size(); j += 1) {
      nLitPixels += (trenchMap[i][j] == '#' ? 1 : 0);
    }
  }
  cout << nLitPixels << endl;
}
