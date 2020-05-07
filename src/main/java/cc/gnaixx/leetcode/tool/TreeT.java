package cc.gnaixx.leetcode.tool;

import cc.gnaixx.leetcode.tool.model.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/**
 * name: TreeT
 * desc: 数工具
 *
 * @author xiangqing.xxq
 * @date 2020/05/07
 */
public class TreeT {
    public static TreeNode createBinaryTree(int[] arrays, int index) {
        TreeNode treeNode = null;
        if (index < arrays.length) {
            treeNode = new TreeNode(
                    arrays[index],
                    createBinaryTree(arrays, 2 * index + 1),
                    createBinaryTree(arrays, 2 * index + 2));
        }
        return treeNode;
    }

    // 前序遍历1
    public static void preOrderTraverse1(TreeNode rootNode, List<Integer> list) {
        if (rootNode == null) return;

        list.add(rootNode.val);
        preOrderTraverse1(rootNode.left, list);
        preOrderTraverse1(rootNode.right, list);
    }

    // 前序遍历2
    public static void preOrderTraverse2(TreeNode rootNode, List<Integer> list) {
        LinkedList<TreeNode> stack = new LinkedList<>();
        TreeNode tmpNode = rootNode;
        while(tmpNode != null || !stack.isEmpty()) {
            if(tmpNode != null) {
                list.add(tmpNode.val);
                stack.push(tmpNode);
                tmpNode = tmpNode.left;
            } else {
                tmpNode = stack.pop();
                tmpNode = tmpNode.right;
            }
        }
    }

    // 中序遍历1
    public static void inOrderTraverse1(TreeNode rootNode, List<Integer> list) {
        if (rootNode == null) return;

        inOrderTraverse1(rootNode.left, list);
        list.add(rootNode.val);
        inOrderTraverse1(rootNode.right, list);
    }

    // 中序遍历2
    public static void inOrderTraverse2(TreeNode rootNode, List<Integer> list) {
        LinkedList<TreeNode> stack = new LinkedList<>();
        TreeNode tmpNode = rootNode;
        while(tmpNode != null || !stack.isEmpty()) {
            if(tmpNode != null) {
                stack.push(tmpNode);
                tmpNode = tmpNode.left;
            } else {
                tmpNode = stack.pop();
                list.add(tmpNode.val);
                tmpNode = tmpNode.right;
            }
        }
    }


    // 后续遍历1
    public static void postOrderTraverse1(TreeNode rootNode, List<Integer> list) {
        if (rootNode == null) return;

        postOrderTraverse1(rootNode.left, list);
        postOrderTraverse1(rootNode.right, list);
        list.add(rootNode.val);
    }

    // 中序遍历2
    public static void postOrderTraverse2(TreeNode rootNode, List<Integer> list) {
        LinkedList<TreeNode> stack = new LinkedList<>();
        TreeNode tmpNode = rootNode;
        while(tmpNode != null || !stack.isEmpty()) {
            if(tmpNode != null) {
                stack.push(tmpNode);
                tmpNode = tmpNode.left;
            } else {
                tmpNode = stack.pop();
                tmpNode = tmpNode.right;
                list.add(tmpNode.val);
            }
        }
    }
}
