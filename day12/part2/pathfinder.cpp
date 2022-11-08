#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
using namespace std;

int getNPaths (string curCave, map<string, int> visited, map<string, vector<string>> &linkMap, string twiceCave) {
  if (curCave == "end") return 1;
  int nPaths = 0;
  vector<string>::iterator neighborIt;
  for (neighborIt = linkMap[curCave].begin(); neighborIt != linkMap[curCave].end(); neighborIt++) {
    string neighbor = *neighborIt;
    if (neighbor == "start") continue;
    if (neighbor == twiceCave && visited[neighbor] > 1) {
      // cout << curCave << " " << neighbor << " " << twiceCave << " " << visited[neighbor] << endl;
      continue;
    };
    if (neighbor != twiceCave && visited[neighbor] > 0 && neighbor[0] >= 'a' && neighbor[0] <= 'z') continue;

    map<string, int> newVisited (visited);
    newVisited[curCave] += 1;
    nPaths += getNPaths(neighbor, newVisited, linkMap, twiceCave);
  }
  return nPaths;
}

int main () {
  ifstream myfile;
  myfile.open ("../testinput");
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
  set<string> smallCaves;
  for (int i = 0; i < numLinks; i++) {
    string link = linkStrings[i];
    int delimeterIndex = link.find_first_of('-');
    string cave1 = link.substr(0, delimeterIndex);
    string cave2 = link.substr(delimeterIndex + 1);
    linkMap[cave1].push_back(cave2);
    linkMap[cave2].push_back(cave1);
    links.push_back(make_pair(cave1, cave2));
    if (cave1[0] >= 'a' && cave1[0] <= 'z' && cave1 != "start" && cave1 != "end") smallCaves.insert(cave1);
    if (cave2[0] >= 'a' && cave2[0] <= 'z' && cave2 != "start" && cave2 != "end") smallCaves.insert(cave2);
  }

  int nPaths = 0;
  set<string>::iterator ptr;  
  for (ptr = smallCaves.begin(); ptr != smallCaves.end(); ptr++) {
    map<string, int> visited;
    visited["start"] = 1;
    nPaths += getNPaths("start", visited, linkMap, *ptr);
  }

  map<string, int> visited;
  visited["start"] = 1;
  int onceCavePaths = getNPaths("start", visited, linkMap, "");
  
  cout << nPaths - ((smallCaves.size() - 1) * onceCavePaths) << endl;
}
