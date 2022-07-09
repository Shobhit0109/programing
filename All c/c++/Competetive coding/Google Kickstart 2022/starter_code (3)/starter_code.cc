#include <bits/stdc++.h>
using namespace std;

// Complete the MinimumDeliveryTime function
int MinimumDeliveryTime(int R, int C, vector <string> grid) {
  int delivery_time = 0;
  // TODO: Add logic to calculate the minimum overall delivery time you can
  // get by building at most one new delivery office.
  return delivery_time;
}

int main() {
  int T;
  // Get the number of test cases
  cin >> T;
  for(int t = 1; t <= T; t++) {
    // Get the dimensions of the grid
    int R, C;
    cin >> R >> C;
    // Get each row of the grid
    vector <string> grid;
    for(int i = 0; i < R; i++) {
      string row;
      cin >> row;
      grid.push_back(row);
    }
    cout << "Case #" << t << ": " << MinimumDeliveryTime(R, C, grid) << "\n";
  }
  return 0;
}
