package cc.gnaixx.leetcode.tool;

import cc.gnaixx.leetcode.tool.model.TreeNode;

import java.util.*;

/**
 * name: TreeT
 * desc: 数工具
 *
 * @author xiangqing.xxq
 * @date 2020/05/07
 */
public class TreeT {
    // 完全二叉树创建
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

    // 前序遍历1 (dfs)
    public static void preOrderTraverse1(TreeNode rootNode, List<Integer> list) {
        if (rootNode == null) return;

        list.add(rootNode.val);
        preOrderTraverse1(rootNode.left, list);
        preOrderTraverse1(rootNode.right, list);
    }

    // 前序遍历2
    public static void preOrderTraverse2(TreeNode rootNode, List<Integer> list) {
        Stack<TreeNode> stack = new Stack<>();

        stack.push(rootNode);
        while(!stack.isEmpty()) {
            TreeNode node = stack.pop();
            list.add(node.val);
            if (node.right != null) stack.push(node.right); // 先入栈右节点
            if (node.left != null) stack.push(node.left);  // 后入栈左节点

        }

        // TreeNode node = rootNode;
        // while(node != null || !stack.isEmpty()) {
        //     if (node != null) {
        //         list.add(node.val);
        //         stack.push(node);
        //         node = node.left;
        //     } else {
        //         node = stack.pop();
        //         node = node.right;
        //     }
        // }
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
        Stack<TreeNode> stack = new Stack<>();
        TreeNode node = rootNode;

        while (node != null || !stack.isEmpty()) {
            while (node != null) {
                stack.push(node);
                node = node.left;
            }
            node = stack.pop();
            list.add(node.val);
            node = node.right;
        }

        // while(node != null || !stack.isEmpty()) {
        //     if(node != null) {
        //         stack.push(node);
        //         node = node.left;
        //     } else {
        //         node = stack.pop();
        //         list.add(node.val);
        //         node = node.right;
        //     }
        // }
    }

    // 后续遍历1
    public static void postOrderTraverse1(TreeNode rootNode, List<Integer> list) {
        if (rootNode == null) return;

        postOrderTraverse1(rootNode.left, list);
        postOrderTraverse1(rootNode.right, list);
        list.add(rootNode.val);
    }

    // 后序遍历2
    public static void postOrderTraverse2(TreeNode rootNode, List<Integer> list) {
        Stack<TreeNode> stack = new Stack<>();

        stack.push(rootNode);
        while(!stack.isEmpty()) {
            TreeNode node = stack.pop();
            if (node != null) {         // 采用和先序遍历一样策略，最后反转
                list.add(node.val);
                stack.push(node.left);
                stack.push(node.right);
            }
        }
        Collections.reverse(list);
    }

    // 层序遍历 (通过队列-bfs)
    public static void levelOrderTraverse(TreeNode rootNode, List<Integer> list) {
        LinkedList<TreeNode> stack = new LinkedList<>();
        stack.add(rootNode);
        while (!stack.isEmpty()) {
            TreeNode node = stack.poll();
            if (node != null) {
                list.add(node.val);
                if (node.left != null) stack.add(node.left);
                if (node.right != null) stack.add(node.right);
            }
        }
    }
}
