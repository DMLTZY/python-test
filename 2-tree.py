class Node(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        # 法二：再添加一个parent属性记录父节点（双向链表），便于路径跟踪，但创建对象时会更复杂


def levelorder(root, node_a, node_b):
    if root is None:
        return
    my_queue = []  # 存储等待遍历的节点
    finded = []  # 存储node_a和node_b的编号
    my_dict = {}  # 存储节点编号与节点的值
    index = 1  # 节点编号
    node = root
    my_queue.append(node)
    my_dict[index] = node.value  # 节点编号:节点的值
    my_dict[node.value] = index  # 节点的值:节点编号
    if node.value == node_a or node.value == node_b:
        finded.append(index)
    while my_queue:  # 逐层遍历二叉树
        node = my_queue.pop(0)
        # print(node.value)
        index = my_dict.pop(node.value) * 2  # 根据上层节点编号建立下层节点的编号
        if node.left is not None:
            my_queue.append(node.left)
            my_dict[index] = node.left.value
            my_dict[node.left.value] = index
            if node.left.value == node_a or node.left.value == node_b:
                finded.append(index)
        index += 1
        if node.right is not None:
            my_queue.append(node.right)
            my_dict[index] = node.right.value
            my_dict[node.right.value] = index
            if node.right.value == node_a or node.right.value == node_b:
                finded.append(index)
    # print(finded)
    # print(my_dict)
    if len(finded) == 0:
        print('Both nodeA and nodeB are not in 2-tree.')
    elif len(finded) == 1:
        print('Either nodeA or nodeB is not in 2-tree, or nodeA is as same as nodeB.')
    elif len(finded) > 2:
        print('2-tree has same value.')
    else:
        trace = []  # 存储最终路径
        parent = False  # 用于标记两节点到root的路径中的第一次相遇
        for i in range(2):
            key = finded[i]
            length = len(trace)
            while key > 0:
                if my_dict.get(key) in trace:  # 删除重复路径
                    if not parent:
                        parent = True
                    else:
                        trace.remove(my_dict.get(key))
                    key //= 2
                    continue
                if i == 0:
                    trace.append(my_dict.get(key))
                else:
                    trace.insert(length, my_dict.get(key))
                key //= 2

        if node_a == trace[0]:  # 根据传参顺序调整最终输出顺序
            print(trace)
        else:
            trace.reverse()
            print(trace)

if __name__ == '__main__':
    # 构建二叉树
    tree = Node('a',
                Node('b', Node('d', Node('f'), Node('g'))),
                Node('c', right=Node('e', Node('h'), Node('i')))
                )
    levelorder(tree, 'd', 'h')


