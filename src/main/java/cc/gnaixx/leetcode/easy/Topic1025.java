package cc.gnaixx.leetcode.easy;

import cc.gnaixx.leetcode.tool.LogT;

/**
 * name: Topic1025
 * desc: 除数博弈
 *
 * @author xiangqing.xxq
 * @date 2020/05/06
 */
public class Topic1025 {
    public boolean divisorGame(int N) {
        // 1.最终结果应该是占到 2 的赢，占到 1 的输；
        // 2.若当前为奇数，奇数的约数只能是奇数或者 1，因此下一个一定是偶数；
        // 3.若当前为偶数，偶数的约数可以是奇数,可以是偶数,也可以是 1，因此直接减 1，则下一个是奇数；
        // 4.因此，奇则输，偶则赢
        // return N % 2 ==0;

        boolean[] must = new boolean[N];
        must[1] = false;
        must[2] = true;
        for (int i = 3; i <= N; i++) {
            for (int j = 1; j < N / 2; j++) {
                if (i % j == 0 && !must[i - j]) { // 如果前一步存在失败情况，则当前一步一定能赢
                    must[i] = true;
                    break;
                }
            }
        }
        return must[N];
    }

    public static void main(String[] args) {
        LogT.print(new Topic1025().divisorGame(1));
        LogT.print(new Topic1025().divisorGame(2));
        LogT.print(new Topic1025().divisorGame(3));
        LogT.print(new Topic1025().divisorGame(4));
        LogT.print(new Topic1025().divisorGame(5));
        LogT.print(new Topic1025().divisorGame(10));
    }
}
