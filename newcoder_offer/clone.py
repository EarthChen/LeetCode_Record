# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
# 另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
# （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        head = pHead
        p_head = None
        new_head = None

        # 保存随机节点和新老节点的字典
        random_dic = {}
        old_new_dic = {}

        # 当头节点不为空时
        while head:
            # 根据旧链表构造一个新节点
            node = RandomListNode(head.label)
            # 将头节点的随机指向的节点赋值给新节点的头节点
            node.random = head.random
            # 将节点对象的内存地址和头节点的id保存到字典中
            old_new_dic[id(head)] = id(node)
            # 将随机节点的对象地址和对象节点保存在随机字典中
            random_dic[id(node)] = node
            # 将头节点的下一个元素赋值给头节点
            head = head.next

            # 如果新头节点存在
            if new_head:
                # 将构造的新节点赋值给头节点的下一个节点
                new_head.next = node
                # 将新头节点的下一个节点赋值给头节点
                new_head = new_head.next
            else:
                # 头新节点不存在时，直接将构造的新节点赋值给头节点
                new_head = node
                # 将新构造的节点赋值给节点
                p_head = node
        new_head = p_head
        # 如果新头节点存在
        while new_head:
            # 并且头节点的随机指针不为空
            if new_head.random is not None:
                # 从随机字典中取出随机节点赋值给头节点的随机指针
                new_head.random = random_dic[old_new_dic[id(new_head.random)]]
            # 将头节点的下一个节点赋值给头结点
            new_head = new_head.next
        # 返回头节点
        return p_head
