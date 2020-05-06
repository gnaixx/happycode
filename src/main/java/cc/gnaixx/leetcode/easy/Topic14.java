package cc.gnaixx.leetcode.easy;

/**
 * name: Topic14
 * desc: 最长前缀
 *
 * @author xiangqing.xxq
 * @date 2020/05/06
 */
public class Topic14 {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        String subString = strs[0];
        for (String str : strs) {
            while (str.indexOf(subString) != 0) {
                subString = subString.substring(0, subString.length() - 1);
            }
        }
        return subString;
    }

    public static void main(String args[]) {
        String sub = new Topic14().longestCommonPrefix(new String[]{"flower", "flow", "flight"});
        System.out.println(sub);

        sub = new Topic14().longestCommonPrefix(new String[]{"dog", "racecar", "car"});
        System.out.println(sub);
    }
}
