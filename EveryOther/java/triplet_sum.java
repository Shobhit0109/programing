import java.util.*;

class triplet_sum {
    public static List<List<Integer>> threeSum(int[] num, int target) {
        Arrays.sort(num);
        Set<List<Integer>> threePairs = new HashSet<>();
        for (int i = 0; i < num.length; i++) { 
            Map<Integer, Integer> zeroMap = new HashMap<>();
            for (int j = 0; j < num.length; j++) {
                if(zeroMap.containsKey(target - num[i] - num[j])) {
                    int k = zeroMap.get(target - num[i] - num[j]);
                    if (k == i || k == j) continue;
                    else {
                        List<Integer> list = new ArrayList<>();
                        list.add(num[i]);
                        list.add(num[k]);
                        list.add(num[j]);
                        threePairs.add(list);
                    }
                }
            zeroMap.put(num[j],j);
            }
        }
        List<List<Integer>> threeSum = new ArrayList<>();
        threeSum.addAll(threePairs);
        return threeSum;
    }
    public static void main(String[] args) {
        System.out.println(threeSum(new int[]{1,2,3,4,5,6,7,8,9,10},12));
    }

}