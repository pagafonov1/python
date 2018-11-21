# Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.

from collections import Counter


class TreeNode:
    def __init__(self, char, weight, left=None, right=None):
        self.char = char
        self.weight = weight
        self.left = left
        self.right = right


def huffman_encode(s):
    # Строку из одного символа и пустую строку не кодируем
    if len(s) < 2:
        return s

    # Из строки строим листья дерева
    def _to_flat_nodes_list(ctr):
        for k, v in ctr:
            yield TreeNode(k, v)

    # Выращиваем дерево из плоского списка листьев
    def _to_tree(nodes_):
        len_ = len(nodes_)

        if len_ == 1:
            return nodes_

        fst = nodes_.pop()
        scd = nodes.pop()

        new_node = TreeNode(None, fst.weight + scd.weight, fst, scd)

        # Сняли два элемента!
        j = len_ - 3

        while True:
            if j < 0 or nodes_[j].weight >= new_node.weight:
                nodes_.insert(j + 1, new_node)
                break
            else:
                j -= 1

        return _to_tree(nodes_)

    # Обходим дерево - строим таблицу
    def _build_table(curr_step, root, table_):
        if root.left is not None:
            _build_table(curr_step + '0', root.left, table_)

        if root.right is not None:
            _build_table(curr_step + '1', root.right, table_)

        if root.char is not None:
            table_[ord(root.char)] = curr_step

        return table_

    nodes = [n for n in _to_flat_nodes_list(Counter(s).most_common())]
    tree = _to_tree(nodes)[0]

    table = dict()
    _build_table('', tree, table)

    return ' '.join([table[ord(c)] for c in s])


# print(huffman_encode("beep boop beer!"))
print(huffman_encode("How much wood would a woodchuck chuck if a woodchuck could chuck wood?"))
