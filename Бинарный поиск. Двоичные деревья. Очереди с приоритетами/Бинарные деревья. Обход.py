#python

def tree_walk():
    tree = [tuple(map(int, input().split())) for _ in range(int(input()))]

    def print_order(node, order):
        if node != -1:
            for f in order:
                yield from f(node, order)

    def print_left(node, order):
        yield from print_order(tree[node][1], order)

    def print_right(node, order):
        yield from print_order(tree[node][2], order)

    def print_key(node, _):
        yield tree[node][0]

    in_order = (print_left, print_key, print_right)
    pre_order = (print_key, print_left, print_right)
    post_order = (print_left, print_right, print_key)
    for d in in_order, pre_order, post_order:
        print(*print_order(0, d))

tree_walk()
