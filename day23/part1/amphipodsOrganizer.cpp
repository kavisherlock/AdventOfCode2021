#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <cmath>
using namespace std;

const int HALLWAY_LENGTH = 11;
const char pods[] = { 'A', 'B', 'C', 'D' };

const int A_ENERGY = 1;
const int ROOM_A_1_IND = 11;
const int ROOM_A_2_IND = 12;
const int HALLWAY_A_IND = 2;

const int B_ENERGY = 10;
const int ROOM_B_1_IND = 13;
const int ROOM_B_2_IND = 14;
const int HALLWAY_B_IND = 4;

const int C_ENERGY = 100;
const int ROOM_C_1_IND = 15;
const int ROOM_C_2_IND = 16;
const int HALLWAY_C_IND = 6;

const int D_ENERGY = 1000;
const int ROOM_D_1_IND = 17;
const int ROOM_D_2_IND = 18;
const int HALLWAY_D_IND = 8;

map<string, int> optimalEnergy;

void prettyPrint(const string &burrow) {
  cout << endl;
  cout << "#############" << endl;
  cout << "#" << burrow.substr(0, HALLWAY_LENGTH) << "#" << endl;
  cout << "###";
  for (int i = ROOM_A_1_IND; i <= ROOM_D_1_IND; i += 2) {
    cout << burrow[i] << "#";
  }
  cout << "##" << endl;
  cout << "  #";
  for (int i = ROOM_A_2_IND; i <= ROOM_D_2_IND; i += 2) {
    cout << burrow[i] << "#";
  }
  cout  << endl;
  cout << "  #########" << endl;
  cout << endl;
}

bool isSolved(const string &burrow) {
  return burrow == "...........AABBCCDD";
}

void moveHallwayPod(string &burrow, int &energy, bool &podMoved, char podType, int podEnergy, int hallwayInd, int room1Ind, int room2Ind) {
  string hallway = burrow.substr(0, HALLWAY_LENGTH);
  if ((burrow[room1Ind] == '.' && burrow[room2Ind] == podType) || burrow[room2Ind] == '.') {
    int podPosition = hallway.find(podType);
    while (podPosition != string::npos) {
      string path;
      if (podPosition < hallwayInd) {
        path = hallway.substr(podPosition + 1, hallwayInd - podPosition);
      } else {
        path = hallway.substr(hallwayInd, podPosition - hallwayInd);
      }
      int pathLength = path.size();
      string emptyPath (pathLength, '.');
      if (path == emptyPath) {
        energy += podEnergy * pathLength;
        burrow[podPosition] = '.';
        if (burrow[room2Ind] == '.') {
          energy += podEnergy * 2;
          burrow[room2Ind] = podType;
          podMoved = true;
        } else if (burrow[room1Ind] == '.') {
          energy += podEnergy;
          burrow[room1Ind] = podType;
          podMoved = true;
        }
      }
      podPosition = hallway.find(podType, podPosition + 1);
    }
  }
}

pair<int, string> moveHallwayPods(const string &burrow) {
  bool podMoved = false;
  int energy = 0;
  string newBurrow(burrow);
  do {
    podMoved = false;
    moveHallwayPod(newBurrow, energy, podMoved, 'A', A_ENERGY, HALLWAY_A_IND, ROOM_A_1_IND, ROOM_A_2_IND);
    moveHallwayPod(newBurrow, energy, podMoved, 'B', B_ENERGY, HALLWAY_B_IND, ROOM_B_1_IND, ROOM_B_2_IND);
    moveHallwayPod(newBurrow, energy, podMoved, 'C', C_ENERGY, HALLWAY_C_IND, ROOM_C_1_IND, ROOM_C_2_IND);
    moveHallwayPod(newBurrow, energy, podMoved, 'D', D_ENERGY, HALLWAY_D_IND, ROOM_D_1_IND, ROOM_D_2_IND);
  } while (podMoved);

  return make_pair(energy, newBurrow);
}

void getSteps(vector<pair<int, string>> &steps, const string &burrow, int roomInd, int hallwayInd, int podEnergy) {
  for (int i = hallwayInd - 1; i >= 0; i -= 1) {
    string newBurrow(burrow);
    if (i != 0 && i % 2 == 0) {
      continue;
    }
    if (newBurrow[i] != '.') {
      break;
    }
    newBurrow[roomInd] = '.';
    newBurrow[i] = burrow[roomInd];
    int pathLength = 2;
    if (roomInd % 2 == 0) {
      pathLength += 1;
    }
    pathLength += hallwayInd - 1 - i;
    int energy = podEnergy * (pathLength);
    steps.push_back(make_pair(energy, newBurrow));
  }
  for (int i = hallwayInd + 1; i < HALLWAY_LENGTH; i += 1) {
    string newBurrow(burrow);
    if (i != HALLWAY_LENGTH - 1 && i % 2 == 0) {
      continue;
    }
    if (newBurrow[i] != '.') {
      break;
    }
    newBurrow[roomInd] = '.';
    newBurrow[i] = burrow[roomInd];
    int pathLength = 2;
    if (roomInd % 2 == 0) {
      pathLength += 1;
    }
    pathLength += i - (hallwayInd + 1);
    int energy = podEnergy * (pathLength);
    steps.push_back(make_pair(energy, newBurrow));
  }
}

vector<pair<int, string>> getAllSteps(const string &burrow) {
  vector<pair<int, string>> steps;
  for (int i = 0; i < 4; i += 1) {
    int roomInd;
    int topRoomInd = HALLWAY_LENGTH + (i * 2);
    int bottomRoomInd = HALLWAY_LENGTH + (i * 2) + 1;
    if (burrow[bottomRoomInd] == '.') {
      continue;
    }
    if (burrow[topRoomInd] == '.') {
      if (burrow[bottomRoomInd] == pods[i]) {
        continue;
      }
      roomInd = bottomRoomInd;
    } else {
      if (burrow[bottomRoomInd] == pods[i] && burrow[topRoomInd] == pods[i]) {
        continue;
      }
      roomInd = topRoomInd;
    }
    char roomPod = burrow[roomInd];
    getSteps(steps, burrow, roomInd, (i * 2) + 2, pow(10, ((int)(roomPod - 'A'))));
  }

  return steps;
}

int findOptimalPath(string burrow) {
  pair<int, string> afterMove = moveHallwayPods(burrow);
  int energy = afterMove.first;
  string newBurrow = afterMove.second;

  if (optimalEnergy.count(newBurrow) > 0) {
    return optimalEnergy[newBurrow];
  }

  if (isSolved(newBurrow)) {
    return energy;
  }

  vector<pair<int, string>> possibleSteps = getAllSteps(newBurrow);
  if (possibleSteps.size() == 0) {
    return 50000;
  }

  int minEnergy = -1;
  for (pair<int, string> step : possibleSteps) {
    pair<int, string> moveAfterStep = moveHallwayPods(step.second);
    int nextEnergy = moveAfterStep.first + step.first + findOptimalPath(moveAfterStep.second);
    if (minEnergy < 0 || minEnergy > nextEnergy) {
      minEnergy = nextEnergy;
    }
  }
  optimalEnergy[newBurrow] = energy + minEnergy;
  return energy + minEnergy;
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

  string burrow = lines[1].substr(1, HALLWAY_LENGTH);
  for (int i = 3; i < 10; i += 2) {
    burrow.push_back(lines[2][i]);
    burrow.push_back(lines[3][i]);
  }

  cout << burrow << endl;
  prettyPrint(burrow);

  cout << findOptimalPath(burrow) << endl;
}
