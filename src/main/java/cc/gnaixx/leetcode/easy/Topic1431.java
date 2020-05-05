package cc.gnaixx.leetcode.easy;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * name: Topic1431
 * desc: 拥有最多糖果的孩子
 *
 * @author: xiangqing
 * @date: 2020/05/05
 */
public class Topic1431 {

    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> res = new ArrayList<>();

        int max = Arrays.stream(candies).max().getAsInt();
        for (int candie : candies) {
            if (candie == max) {
                res.add(true);
                continue;
            }
            if (candie + extraCandies >= max) res.add(true);
            if (candie + extraCandies < max) res.add(false);
        }
        return res;
    }


    public static void main(String[] args) {
        List<Boolean> res = new Topic1431().kidsWithCandies(new int[]{2, 3, 5, 1, 3}, 3);
        System.out.println(res);
    }
}
