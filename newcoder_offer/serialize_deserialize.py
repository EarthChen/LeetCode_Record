# 请实现两个函数，分别用来序列化和反序列化二叉树


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    flag = -1

    def Serialize(self, root):
        """
        对于序列化：使用前序遍历，递归的将二叉树的值转化为字符，并且在每次二叉树的结点
        不为空时，在转化val所得的字符之后添加一个' ， '作为分割。对于空节点则以 '#' 代替
        :param root:
        :return:
        """
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        """
        对于反序列化：按照前序顺序，递归的使用字符串中的字符创建一个二叉树
        :param s:
        :return:
        """
        self.flag += 1

        l = s.split(',')
        if self.flag >= len(s):
            return None

        root = None
        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root
