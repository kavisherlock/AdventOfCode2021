#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int getNPaths (string curCave, map<string, bool> visited, map<string, vector<string>> &linkMap) {
  if (curCave == "end") return 1;
  int nPaths = 0;
  vector<string>::iterator neighborIt;
  for (neighborIt = linkMap[curCave].begin(); neighborIt != linkMap[curCave].end(); neighborIt++) {
    string neighbor = *neighborIt;
    if (visited[neighbor]) continue;

    map<string, bool> newVisited (visited);
    newVisited[curCave] = (curCave[0] >= 'a' && curCave[0] <= 'z');
    nPaths += getNPaths(neighbor, newVisited, linkMap);
  }
  return nPaths;
}

int main () {
  ifstream myfile;
  myfile.open ("../input");
  vector<string> linkStrings;
  if (myfile.is_open()) {
    string mystring;
    while(getline(myfile, mystring)) {
      linkStrings.push_back(mystring);
    }
  }
  myfile.close();

  vector<pair<string, string>> links;
  map<string, vector<string>> linkMap;
  int numLinks = linkStrings.size();
  for (int i = 0; i < numLinks; i++) {
    string link = linkStrings[i];
    int delimeterIndex = link.find_first_of('-');
    string cave1 = link.substr(0, delimeterIndex);
    string cave2 = link.substr(delimeterIndex + 1);
    linkMap[cave1].push_back(cave2);
    linkMap[cave2].push_back(cave1);
    links.push_back(make_pair(cave1, cave2));
  }

  map<string, bool> visited;
  visited["start"] = true;
  cout << getNPaths("start", visited, linkMap) << endl;
}
