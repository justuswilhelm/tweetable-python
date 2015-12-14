count_leaves = lambda l: 1 if not l[1] else sum(count_leaves(e) for e in l[1])
assert count_leaves([3, [[2, [[1, []]]], [5, [[7, []]]]]]) == 2
