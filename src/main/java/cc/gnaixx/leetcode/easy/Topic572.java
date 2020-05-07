package cc.gnaixx.leetcode.easy;

import cc.gnaixx.leetcode.tool.LogT;
import cc.gnaixx.leetcode.tool.model.TreeNode;

import java.util.ArrayList;
import java.util.List;

import static cc.gnaixx.leetcode.tool.TreeT.*;

/**
 * name: Topic572
 * desc: 另一个树的子树
 *
 * @author xiangqing.xxq
 * @date 2020/05/07
 */
public class Topic572 {
    public boolean isSameTree(TreeNode s, TreeNode t) {
        if (s == null && t == null) return true;
        if (s == null || t == null) return false;
        if (s.val != t.val) return false;
        return isSameTree(s.left, t.left) && isSameTree(s.right, t.right);
    }

    public boolean isSubtree(TreeNode s, TreeNode t) {
        if (t == null) return true;
        if (s == null) return false;
        return isSubtree(s.left, t) || isSubtree(s.right, t) || isSameTree(s, t);
    }


    public static void main(String[] args) {
        TreeNode treeNodeA = createBinaryTree(new int[]{3, 4, 5, 1, 2}, 0);
        TreeNode treeNodeB = createBinaryTree(new int[]{4, 1, 2}, 0);

        LogT.print(new Topic572().isSubtree(treeNodeA, treeNodeB));

        List<Integer> treeList = new ArrayList<>();
        preOrderTraverse1(treeNodeA, treeList);
        LogT.print(treeList.toString());

        treeList.clear();
        preOrderTraverse2(treeNodeB, treeList);
        LogT.print(treeList.toString());

        treeList.clear();
        inOrderTraverse1(treeNodeA, treeList);
        LogT.print(treeList.toString());

        treeList.clear();
        inOrderTraverse2(treeNodeA, treeList);
        LogT.print(treeList.toString());

        treeList.clear();
        postOrderTraverse1(treeNodeA, treeList);
        LogT.print(treeList.toString());

        treeList.clear();
        postOrderTraverse2(treeNodeA, treeList);
        LogT.print(treeList.toString());
    }
}
