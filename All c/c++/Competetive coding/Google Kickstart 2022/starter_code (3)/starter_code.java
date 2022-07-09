import java.io.*;
import java.util.*;

public class Solution {
  private static int minimumDeliveryTime(int[][] deliveryOffices) {
    // TODO: solve for and return the minimum overall delivery time you can get
    // by building at most one new delivery office
    return 0;
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int T = scanner.nextInt();

    for (int testCase = 0; testCase < T; ++testCase) {
      int R = scanner.nextInt();
      int C = scanner.nextInt();
      int[][] deliveryOffices = new int[R][C];

      for (int row = 0; row < R; ++row) {
        String line = scanner.next();
        for (int col = 0; col < C; ++col) {
          deliveryOffices[row][col] = line.charAt(col) - '0'; // converts char to int
        }
      }

      System.out.println("Case #" + testCase + ": " + minimumDeliveryTime(deliveryOffices));
    }
  }
}
