# 二叉树的叶子结点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        """
        判断二叉树是否为空
        :return:
        """
        if self.root is None:
            return True
        return False

    # def create(root):
    #     a = input('enter a key:');
    #     if a is '#':
    #         root = None
    #     else:
    #         root = TreeNode(a)
    #         root.left = create(root.left)
    #         root.right = create(root.right)
    #     return root

    def create(self, node):
        temp = input('enter a value:')
        if temp is '#':
            node = None
        else:
            node = TreeNode(temp)
            node.left = self.create(node.left)
            node.right = self.create(node.right)
        return node
        # return node
        # treenode = TreeNode(temp)
        # if self.root is 0:
        #     self.root = treenode
        #
        # treenode.left = self.create()
        # treenode.right = self.create()

    def pre_order(self, tree_node):
        """
        前序遍历
        :param tree_node: tree_nodeNode
        :return:
        """
        if tree_node is None:
            return
        print(tree_node.val, end=' ')
        self.pre_order(tree_node.left)
        self.pre_order(tree_node.right)

    def mid_order(self, tree_node):
        """
        中序遍历
        :param tree_node: tree_nodeNode
        :return:
        """
        if tree_node is None:
            return
        self.pre_order(tree_node.left)
        print(tree_node.val, end=' ')
        self.pre_order(tree_node.right)

    def later_order(self, tree_node):
        """
        后序遍历
        :param tree_node: tree_nodeNode
        :return:
        """
        if tree_node is None:
            return
        self.pre_order(tree_node.left)
        self.pre_order(tree_node.right)
        print(tree_node.val, end=' ')


# def preorder(root):  # 前序遍历
#     if root is None:
#         return
#     else:
#         print(root.val)
#         preorder(root.left)
#         preorder(root.right)


if __name__ == '__main__':
    # root = create(None)
    # preorder(root)
    tree = BinaryTree()
    tree.root = tree.create(tree.root)
    tree.pre_order(tree.root)
    tree.mid_order(tree.root)
    tree.later_order(tree.root)
