# Закодировать любую строку по алгоритму Хаффмана.
from collections import Counter


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(head, codes=dict(), code=''):
    if head is None:
        return None
    if isinstance(head.value, str):
        codes[head.value] = code
        return codes
    get_code(head.left, codes, code+'0')
    get_code(head.right, codes, code+'1')

    return codes


def get_tree(temp):
    count_str = Counter(temp)
    if len(count_str) <= 1:
        node = Node(None)
        if len(count_str) == 1:
            node.left = Node(count_str[0])
            node.right = None
        count_str = {node: 1}
    while len(count_str) != 1:
        node = Node(None)
        spam = count_str.most_common()[:-3:-1]
        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])
        else:
            node.left = spam[0][0]
        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])
        else:
            node.right = spam[1][0]
        del count_str[spam[0][0]]
        del count_str[spam[1][0]]
        count_str[node] = spam[0][1] + spam[1][1]
    return [key for key in count_str][0]


def coding(string, codes):
    res = ''
    for symbol in string:
        res += codes[symbol]
    return res


if __name__ == '__main__':
    test_str = 'test text'
    tree = get_tree(test_str)
    cod = get_code(tree)
    print(cod)

    coding_str = coding(test_str, cod)
    print(coding_str)
