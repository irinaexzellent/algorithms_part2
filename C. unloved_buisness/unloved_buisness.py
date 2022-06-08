class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, idx):
    head = node
    if idx == 0:
        head = head.next_item
    else:
        while idx:
            prev_node = node
            if node.next_item is None:
                print('Wrong index')
                return head
            else:
                node = node.next_item
                idx -= 1
        prev_node.next_item = node.next_item
    return head


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    while new_head:
        print(new_head.value, end="\n")
        new_head = new_head.next_item
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()
