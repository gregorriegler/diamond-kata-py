chars = ["A", "B", "C", "D"]
whitespace = " "


def diamond(basis):
    top = build_top(basis)
    bottom = top[::-1]
    return top + middle(basis) + bottom


def middle(basis):
    if chars.index(basis) == 0:
        return [basis]
    else:
        return [basis + middle_space(basis) + basis]


def build_top(basis):
    index = chars.index(basis)
    for_top = chars_for_top(basis)
    top = []
    for idx, char in enumerate(for_top):
        if idx == 0:
            top.append(space(index) + char + space(index))
        else:
            top.append(space(index - idx) + char + space(fun1357(idx)) + char + space(index - idx))
    return top


def chars_for_top(basis):
    return chars[0:chars.index(basis)]


def middle_space(basis):
    return space(fun1357(chars.index(basis)))


def space(size):
    outer_space = whitespace * size
    return outer_space


def fun1357(i):
    return (i - 1) * 2 + 1
