# 单链表结点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 单链表
class LinkList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        """
        判断单链表是否为空
        :return: bool
        """
        return self._head is None

    def print(self):
        """
        打印所有所有结点的值
        :return:
        """
        p = self._head
        while p:
            print(p.val, end=' ')
            p = p.next
        print()

    def prepend(self, val):
        """
        头插法
        :param val:
        :return:
        """
        temp = ListNode(val)
        temp.next(self._head)
        self._head = temp

    def append(self, val):
        """
        尾插发
        :param val:
        :return:
        """
        temp = ListNode(val)
        if self.is_empty():
            # 若为空表，将添加的元素设为第一个元素
            self._head = temp
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = temp

    def get_length(self):
        """
        得到链表的长度
        :return:
        """
        p = self._head
        length = 0
        while p is not None:
            length += 1
            p = p.next
        return length

    def search(self, val):
        """
        检索元素是否在链表中
        :param val: 结点的值
        :return: bool
        """
        current = self._head
        while current is not None:
            if current.val == val:
                return True
            else:
                current = current.next
        return False

    def insert(self, index, val):
        try:
            index = int(index)
        except Exception:
            print('index不合法')
            return
        if index > self.get_length() or index < 1:
            print('索引不合法')
            return
        else:
            temp = ListNode(val)
            current = self._head
            if index == 1:
                temp.next = self._head
                self._head = temp
                return
            else:
                for i in range(1, index - 1):
                    current = current.next
                temp.next = current.next
                current.next = temp
                return

    def remove(self, index):
        """
        删除链表中某个位置的节点
        :param index: 索引位置
        :return:
        """
        try:
            index = int(index)
        except Exception:
            print('index不合法')
            return
        if index > self.get_length() or index < 0:
            print('索引不合法')
            return
        else:
            if index == 0:
                self._head = self._head.next
            else:
                current = self._head
                for i in range(1, index - 1):
                    current = current.next
                temp = current.next
                current.next = temp.next

    def clear(self):
        """
        情况链表
        :return:
        """
        self._head = None


if __name__ == '__main__':
    link = LinkList()
    for i in range(10):
        link.append(i)
    link.print()
    print('{}是否存在链表里{}'.format(5, link.search(5)))
    link.remove(4)
    print('删除第{}个索引之后元素为'.format(2))
    link.print()
    link.insert(3, 10)
    print('插入在索引为3位置之后为')
    link.print()
    print('当前链表长度为', link.get_length())
    link.clear()
