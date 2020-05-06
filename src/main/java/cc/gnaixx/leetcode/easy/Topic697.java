package cc.gnaixx.leetcode.easy;

import java.util.HashMap;
import java.util.Map;

/**
 * name: Topic697
 * desc: 数组的度
 *
 * @author: xiangqing
 * @date: 2020/05/03
 */
public class Topic697 {
    static class Node {
        public int degree;
        public int start;
        public int end;
    }

    public int findShortestSubArray(int[] nums) {
        Map<String, Node> nodeMap = new HashMap<>();
        int maxDegree = 0;
        int minLength = 50000;

        for (int i = 0; i < nums.length; i++) {
            Node node = nodeMap.get(String.valueOf(nums[i]));
            if (node == null) {
                node = new Node();
                nodeMap.put(String.valueOf(nums[i]), node);
            }

            if (node.degree == 0) {
                node.start = i;
            }
            node.end = i;
            node.degree++;
            if (maxDegree < node.degree) maxDegree = node.degree;
        }

        for(String key: nodeMap.keySet()) {
            Node node = nodeMap.get(key);
            if (node.degree < maxDegree) continue;
            minLength = Math.min(minLength, node.end - node.start + 1);
        }

        return minLength;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 2, 3, 1};
        int length = new Topic697().findShortestSubArray(nums);
        System.out.println(length);

        int[] nums2 = {1, 2, 2, 3, 1, 4, 2};
        int length2 = new Topic697().findShortestSubArray(nums2);
        System.out.println(length2);
    }
}
