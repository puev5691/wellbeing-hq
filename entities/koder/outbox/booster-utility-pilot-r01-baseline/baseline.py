def runs(s):
    result = []
    for char in s:
        if result and result[-1][0] == char and result[-1][1] < 3:
            result[-1] = (char, result[-1][1] + 1)
        else:
            result.append((char, 1))
    return result
