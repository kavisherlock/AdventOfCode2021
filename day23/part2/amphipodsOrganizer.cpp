#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <cmath>
using namespace std;

const int HALLWAY_LENGTH = 11;
const int N_PODS_PER_ROOM = 4;
const int N_POD_TYPES = 4;
const int N_ROOMS = N_POD_TYPES;
char PODS[N_POD_TYPES];
int ROOM_INDS[N_ROOMS][N_PODS_PER_ROOM];

map<string, int> optimalEnergy;

// Initialise the burrow and pod indices
void initialise() {
  for (int p = 0; p < N_POD_TYPES; p += 1) {
    PODS[p] = 'A' + p;
  }
  for (int p = 0; p < N_PODS_PER_ROOM; p += 1) {
    for (int r = 0; r < N_ROOMS; r += 1) {
      ROOM_INDS[r][p] = HALLWAY_LENGTH + (N_PODS_PER_ROOM * r) + p;
    }
  }
}

// Print your string burrow nicely
void prettyPrint(const string &burrow) {
  cout << endl;
  cout << "#############" << endl;
  cout << "#" << burrow.substr(0, HALLWAY_LENGTH) << "#" << endl;
  cout << "###";
  for (int p = 0; p < N_PODS_PER_ROOM; p += 1) {
    if (p != 0) cout << "  #";
    for (int t = 0; t < N_POD_TYPES; t += 1) {
      cout << burrow[ROOM_INDS[t][p]] << "#";
    }
    if (p == 0) cout << "##";
    cout << endl;
  }
  cout << "  #########" << endl;
  cout << endl;
}

// Check if burrow is solved
bool isSolved(const string &burrow) {
  string emptyHallway(HALLWAY_LENGTH, '.');
  if (burrow.substr(0, HALLWAY_LENGTH) != emptyHallway) {
    return false;
  }
  for (int r = 0; r < N_ROOMS; r += 1) {
    string fullRoom(N_PODS_PER_ROOM, PODS[r]);
    if (burrow.substr(HALLWAY_LENGTH + (r * N_PODS_PER_ROOM), N_PODS_PER_ROOM) != fullRoom) {
      return false;
    }
  }
  return true;
}

// Move the pod of type podTypeInd from the hallway to the room, if possible
void moveHallwayPod(string &burrow, int &energy, bool &podMoved, int podTypeInd) {
  char podType = PODS[podTypeInd];
  int podEnergy = pow(10, podTypeInd);
  int hallwayInd = 2 + (2 * podTypeInd);
  int roomInds[N_PODS_PER_ROOM];
  for (int i = 0; i < N_PODS_PER_ROOM; i += 1) {
    roomInds[i] = ROOM_INDS[podTypeInd][i];
  }
  string hallway = burrow.substr(0, HALLWAY_LENGTH);

  // Check if Room is empty or has only the right pods
  string room = burrow.substr(roomInds[0], N_PODS_PER_ROOM);
  for (char r : room) {
    if (r != '.' &&  r != podType) {
      return;
    }
  }

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
      burrow[podPosition] = '.';
      int firstAvailableRoom = roomInds[0];
      for (int i = 1; i < N_PODS_PER_ROOM; i += 1) {
        if (burrow[roomInds[i]] != '.') break;
        firstAvailableRoom = roomInds[i];
      }
      energy += podEnergy * (pathLength + 1 + firstAvailableRoom - roomInds[0]);
      podMoved = true;
      burrow[firstAvailableRoom] = podType;
    }
    podPosition = hallway.find(podType, podPosition + 1);
  }
}

// Move all possible pods from the hallway to the room
pair<int, string> moveHallwayPods(const string &burrow) {
  bool podMoved = false;
  int energy = 0;
  string newBurrow(burrow);
  do {
    podMoved = false;
    for (int p = 0; p < N_POD_TYPES; p += 1) {
      moveHallwayPod(newBurrow, energy, podMoved, p);
    }
  } while (podMoved);

  return make_pair(energy, newBurrow);
}

// Get all the steps for pod on roomInd, given its energy and depth in room
void getSteps(vector<pair<int, string>> &steps, const string &burrow, int roomInd, int hallwayInd, int podEnergy, int podDepth) {
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
    pathLength += podDepth;
    pathLength += hallwayInd - 1 - i;
    int energy = podEnergy * pathLength;
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
    pathLength += podDepth;
    pathLength += i - (hallwayInd + 1);
    int energy = podEnergy * pathLength;
    steps.push_back(make_pair(energy, newBurrow));
  }
}

// Get all possible steps in burrow for all rooms
vector<pair<int, string>> getAllSteps(const string &burrow) {
  vector<pair<int, string>> steps;
  
  for (int r = 0; r < N_ROOMS; r += 1) {
    int roomInds[N_PODS_PER_ROOM];
    for (int i = 0; i < N_PODS_PER_ROOM; i += 1) {
      roomInds[i] = ROOM_INDS[r][i];
    }
    char firstPod = '.';
    char firstPodInd = -1;
    bool canMove = false;
    for (int i : roomInds) {
      if (burrow[i] != '.' && firstPod == '.') {
        firstPod = burrow[i];
        firstPodInd = i;
      }
      if (burrow[i] != '.' && burrow[i] != PODS[r]) {
        canMove = true;
      }
    }
    if (!canMove) continue;

    getSteps(steps, burrow, firstPodInd, (r * 2) + 2, pow(10, ((int)(firstPod - 'A'))), firstPodInd - roomInds[0]);
  }

  return steps;
}

// Returns optimal energy required to solve the burrow
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

  initialise();

  string burrow = lines[1].substr(1, HALLWAY_LENGTH);
  string extraLines[] = { "  #D#C#B#A#", "  #D#B#A#C#" };
  for (int i = 3; i < 10; i += 2) {
    burrow.push_back(lines[2][i]);
    burrow.push_back(extraLines[0][i]);
    burrow.push_back(extraLines[1][i]);
    burrow.push_back(lines[3][i]);
  }

  cout << burrow << endl;
  prettyPrint(burrow);

  cout << findOptimalPath(burrow) << endl;
}
