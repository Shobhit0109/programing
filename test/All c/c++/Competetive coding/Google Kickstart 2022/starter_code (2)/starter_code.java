import java.io.*;
import java.util.*;

public class Solution {

  private static boolean containsSpell(String expression) {
    // TODO: implement this method to return if the expression contains a spell.
    return false;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int caseNum = in.nextInt(); // Scanner has functions to read ints, longs, strings, chars, etc.
    for (int t = 1; t <= caseNum; ++t) {
      String expression = in.next();
      System.out.println("Case #" + t + ": " + (containsSpell(expression) ? "Spell!" : "Nothing."));
    }
  }
}
