package cc.gnaixx.leetcode.tool.model;

import cc.gnaixx.leetcode.easy.Topic572;

/**
 * name: TreeNode
 * desc: 树节点
 *
 * @author xiangqing.xxq
 * @date 2020/05/07
 */
public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;

    public TreeNode() { }

    public TreeNode(int val) {
        this.val = val;
    }

    public TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
