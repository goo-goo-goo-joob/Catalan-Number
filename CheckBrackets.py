def check(brackets):
    if len(brackets) > 80:
        return 4
    j = 0
    for i in range(len(brackets)):
        if brackets[i] == '(':
            j += 1
        elif brackets[i] == ')':
            j -= 1
        else:
            return 2
        if j < 0:
            return 1
    if j != 0:
        return 1
    return 0
