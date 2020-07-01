class Node:
    def __init__(self, data):
        self.data = data  # 表示对应的元素
        self.left = None  # 表示左节点
        self.right = None  # 表示右节点

    def __repr__(self): # 重写方法
        return f"Node({self.data})"


class Tree:
    def __init__(self):
        self.root = None  # 链表的头结点定义为根节点 root

    def add(self, item):
        node = Node(item) # 构造新结点
        if self.root is None:  # 如果二叉树为空，那么生成的二叉树最终为新插入树的点
            self.root = node
        else:
            temp = [self.root]  # 保存结点
            while True:
                pop_node = temp.pop(0) # 弹出 temp 第一个结点,进行判断
                if pop_node.left is None:  # 左子树为空则将点添加到左子树
                    pop_node.left = node
                    return
                elif pop_node.right is None:  # 右子树为空则将点添加到右子树
                    pop_node.right = node
                    return
                else: # 当一个中间结点下,左右子树都不为空时,将左右子树添加到 temp 里面,进行下一次的弹出判断
                    temp.append(pop_node.left)  # 添加左子树结点
                    temp.append(pop_node.right) # 添加右子树结点

    def get_parent(self, item):
        if self.root.data == item: # 当传入的结点为根节点时,此时根节点没有父节点返回 None
            return None  # 根节点没有父节点
        temp = [self.root] # 如果不等于父节点,将根节点保存下来,向下级开始查找
        while temp:
            pop_node = temp.pop(0) # 弹出 temp 列表的第一个结点,去查找左右子树
            if pop_node.left.data == item:  # 某点的左子树为寻找的点
                return pop_node  # 返回某点，即为寻找点的父节点
            if pop_node.right.data == item:  # 某点的右子树为寻找的点
                return pop_node  # 返回某点，即为寻找点的父节点
            if pop_node.left:  # 如果上面的左右子树都不等于 tiem 那么将左右子树添加到tmp,当做中间结点继续向下查找
                temp.append(pop_node.left)
            if pop_node.right:
                temp.append(pop_node.right)
        return None

    def get_parent1(self, item):
        if self.root.data == item:
            return None
        res = []
        temp = [self.root]
        while temp:
            pop_node = temp.pop(0)
            if pop_node.left and (pop_node.left.data == item):
                res.append(pop_node)
            elif pop_node.right and (pop_node.right.data == item):
                res.append(pop_node)
            if pop_node.left: # 如果当前结点有左结点,收集起来待遍历
                temp.append(pop_node.left)
            if pop_node.right:  # 如果当前结点有右节点,收集起来待遍历
                temp.append(pop_node.right)
        return res

    def delete(self, item):
        if self.root is None:  # 如果根为空，就什么也不做
            raise Exception('空树你删个毛线')

        parent = self.get_parent(item)
        if parent:
            del_node = None  # 待删除结点
            if parent.left.data == item:
                del_node = parent.left
            elif parent.right.data == item:
                del_node = parent.right

            if del_node.left is None:  # 左子树为空
                if parent.left.data == item:  # 如果该结点是是左孩子
                    parent.left = del_node.right  #
                else:
                    parent.right = del_node.right
                del del_node
                return True
            elif del_node.right is None:  # 有子树为空
                if parent.left.data == item:
                    parent.left = del_node.left
                else:
                    parent.right = del_node.left
                del del_node
                return True
            else:  # 左右子树都不为空
                tmp_pre = del_node
                tmp_next = del_node.right
                if tmp_next.left is None:
                    # 替代
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right

                else:
                    while tmp_next.left:  # 让tmp指向右子树的最后一个叶子
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    # 替代
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                if parent.left.item == item:
                    parent.left = tmp_next
                else:
                    parent.right = tmp_next
                del del_node
                return True
        else:
            return False

    def __repr__(self):
        res = ''
        curr = self.root
        while tree:
            res += f'{curr} -->'
            curr = curr.left
        return res


if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    print(tree.root.left.left)
    print(tree.root.left.right)
    print(tree.get_parent(2))
    print(tree.get_parent1(2))
    tree.delete(5)
    print(tree.root.left.right)
